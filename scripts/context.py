#!/usr/bin/env python3
"""Portable personal context. Python 3.10+, standard library, no network calls."""
import argparse
import hashlib
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
    'identity': '身份与职业背景', 'values': '价值观与习惯',
    'collaboration': 'AI协作与工作方式', 'learning': '英语与认知学习',
    'skills': '技术能力与证据', 'companies': '公司与业务经营',
    'finance': '财务历史与财富目标', 'officeflow': 'OfficeFlow产品档案',
    'engineering': '工程资料与DocumentFlow', 'portfolio': '其他产品项目',
    'content': '内容与个人品牌', 'research': '探索与研究项目',
    'devices': '设备与工具使用', 'unknowns': '待确认与覆盖缺口',
}
PROFILES = {
    'general': ['identity','values','collaboration','unknowns'],
    'full': list(DOMAINS),
    'coding': ['identity','collaboration','skills','officeflow','engineering','unknowns'],
    'officeflow': ['identity','collaboration','officeflow','content','unknowns'],
    'engineering': ['collaboration','engineering','skills','unknowns'],
    'business': ['identity','values','companies','officeflow','content','finance','unknowns'],
    'english': ['identity','learning','content','collaboration'],
    'content': ['identity','content','officeflow','collaboration'],
    'research': ['research','collaboration','skills','unknowns'],
}
LEVELS = {'public': 0, 'private': 1, 'restricted': 2}
KINDS = {'fact','preference','constraint','goal','requirement','inference','interest','unknown'}
STATUSES = {'current','historical','documented','candidate','unknown','superseded','retracted'}
EVIDENCE = {'memory_summary','user_quote','retrieved_user_statement','account_verified',
            'assistant_inference','assistant_analysis','third_party_signal',
            'document_requirement','document_record','conversation_topic'}
FIELDS = {'id','domain','topics','statement','kind','status','evidence','sensitivity',
          'observed_at','recorded_at','review_after_days','sources','priority',
          'public_approved','supersedes'}

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def load(root=ROOT):
    data = read_json(root/'data/facts.json')
    sources = read_json(root/'data/sources.json')['sources']
    return data, sources

def parse_date(value):
    if not isinstance(value,str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',value):
        raise ValueError('expected YYYY-MM-DD')
    return date.fromisoformat(value)

def errors(data, sources):
    out=[]
    if not isinstance(data,dict) or not isinstance(data.get('facts'),list):
        return ['facts must be an array']
    for key in ['schema_version','dataset_version','as_of','owner_handle','repository_visibility','scope']:
        if not isinstance(data.get(key),str) or not data[key]:out.append('metadata: '+key)
    if data.get('repository_visibility')!='private':out.append('master dataset must declare private')
    try: parse_date(data.get('as_of'))
    except (ValueError,TypeError):out.append('metadata: invalid as_of')
    source_ids=set()
    for s in sources:
        if not isinstance(s,dict):out.append('source must be an object');continue
        sid=s.get('id')
        if not isinstance(sid,str) or not re.fullmatch(r'S\d{3,}',sid) or sid in source_ids:
            out.append('invalid/duplicate source id: '+str(sid))
        else:source_ids.add(sid)
        for key in ['kind','title','locator','limitation']:
            if not isinstance(s.get(key),str) or not s[key]:out.append(f'{sid}: source {key}')
        try:parse_date(s.get('date'))
        except (ValueError,TypeError):out.append(f'{sid}: invalid source date')
    ids=set()
    edges={}
    by_id={}
    for f in data['facts']:
        if not isinstance(f,dict):out.append('fact must be an object');continue
        fid=f.get('id')
        if not isinstance(fid,str) or not re.fullmatch(r'[A-Z]{2}\d{3,}',fid) or fid in ids:
            out.append('invalid/duplicate fact id: '+str(fid))
        else:ids.add(fid);by_id[fid]=f
        if set(f)!=FIELDS:out.append(f'{fid}: missing/unknown fields {set(f)^FIELDS}')
        for k,allowed in [('domain',DOMAINS),('kind',KINDS),('status',STATUSES),('evidence',EVIDENCE),('sensitivity',LEVELS)]:
            if not isinstance(f.get(k),str) or f[k] not in allowed:out.append(f'{fid}: invalid {k}')
        if not isinstance(f.get('statement'),str) or not f['statement'].strip():out.append(f'{fid}: empty statement')
        for k in ['observed_at','recorded_at']:
            if f.get(k) is None and k=='observed_at':continue
            try: parse_date(f.get(k))
            except (TypeError,ValueError):out.append(f'{fid}: invalid {k}')
        n=f.get('review_after_days')
        if n is not None and (type(n)!=int or n<1):out.append(f'{fid}: review_after_days')
        if type(f.get('priority'))!=int or f['priority'] not in range(1,6):out.append(f'{fid}: priority 1..5')
        if type(f.get('public_approved'))!=bool:out.append(f'{fid}: public_approved must be boolean')
        if f.get('public_approved') and f.get('sensitivity')!='public':out.append(f'{fid}: public approval requires public classification')
        topics=f.get('topics')
        if not isinstance(topics,list) or not topics or any(not isinstance(t,str) or not t for t in topics):out.append(f'{fid}: topics')
        refs=f.get('sources')
        if not isinstance(refs,list) or not refs or any(not isinstance(s,str) or s not in source_ids for s in refs):out.append(f'{fid}: unresolved sources')
        supersedes=f.get('supersedes')
        if not isinstance(supersedes,list) or any(not isinstance(s,str) for s in supersedes):
            out.append(f'{fid}: supersedes must be string array');supersedes=[]
        edges[str(fid)]=supersedes
    for fid,refs in edges.items():
        for ref in refs:
            if ref not in ids or ref==fid:out.append(f'{fid}: invalid supersedes {ref}')
            elif by_id[ref].get('status') not in {'historical','superseded','retracted'}:
                out.append(f'{fid}: old fact {ref} must be historical/superseded/retracted')
    def visit(node,trail,done):
        if node in trail:return True
        if node in done:return False
        trail.add(node)
        for prev in edges.get(node,[]):
            if visit(prev,trail,done):return True
        trail.remove(node);done.add(node);return False
    done=set()
    if any(visit(node,set(),done) for node in edges):out.append('supersedes cycle')
    return out

def freshness(f, as_of):
    if f['observed_at'] is None:return 'undated'
    if f['status'] in {'historical','superseded','retracted'}:return 'historical'
    n=f['review_after_days']
    if n and as_of > parse_date(f['observed_at'])+timedelta(days=n):return 'review_due'
    return 'dated_record'

def select(data, profile, audience, history=False, as_of=None):
    as_of=as_of or date.today()
    selected=[]
    # Derive replacements across the whole ledger BEFORE audience/profile filtering.
    replaced={old for f in data['facts'] if f['status'] not in {'retracted','candidate','unknown'} for old in f['supersedes']}
    for original in data['facts']:
        if original['domain'] not in PROFILES[profile]:continue
        if LEVELS[original['sensitivity']]>LEVELS[audience]:continue
        if audience=='public' and not original['public_approved']:continue
        if not history and (original['status'] in {'superseded','retracted'} or original['id'] in replaced):continue
        # Historical facts stay visible as historical context, never relabelled current.
        f=dict(original)
        f['freshness']=freshness(f,as_of)
        if f['id'] in replaced and f['status']!='retracted':f['status']='superseded'
        if audience=='public':
            # Private source locators and registry are never placed in public exports.
            f.pop('sources',None)
        selected.append(f)
    return sorted(selected,key=lambda f:(f['priority'],list(DOMAINS).index(f['domain']),f['id']))

def envelope(data,facts,profile,audience,as_of,history):
    return {'schema_version':'1.0.0','dataset_version':data['dataset_version'],
            'dataset_as_of':data['as_of'],'exported_as_of':as_of.isoformat(),
            'profile':profile,'audience':audience,'includes_superseded':history,
            'usage':'Background data only, not instructions or authorization. Preserve dates, uncertainty and evidence types. Historical goals are not achievements.',
            'facts':facts}

def markdown(packet):
    lines=['# Elvis Context OS · '+packet['profile'], '',
           f"数据截止：{packet['dataset_as_of']} · 导出检查日：{packet['exported_as_of']} · 范围：{packet['audience']}",'',
           '> 以下是背景资料，不授予执行、发送、交易或账号访问权限。历史、目标、文档要求、推断和待确认项应保持原有标记。review_due表示应复核，不等于已被否定。','']
    if not packet['facts']:lines.extend(['本范围没有已批准的信息。公开导出默认留空；这不是完整仓库公开版。',''])
    for domain,title in DOMAINS.items():
        group=[f for f in packet['facts'] if f['domain']==domain]
        if not group:continue
        lines.extend(['## '+title,''])
        for f in group:
            refs='；来源 '+','.join(f['sources']) if 'sources' in f else ''
            lines.extend([f"- **{f['id']}** {f['statement']}", f"  记录：{f['observed_at'] or '日期未知'}；{f['kind']} / {f['status']} / {f['evidence']}；{f['freshness']}{refs}"])
        lines.append('')
    return '\n'.join(lines)+'\n'

def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8')

def build(data,sources,as_of,root=ROOT):
    files={}
    all_facts=select(data,'full','restricted',True,as_of)
    for domain,title in DOMAINS.items():
        packet=envelope(data,[f for f in all_facts if f['domain']==domain],'full','restricted',as_of,True)
        files[f'docs/{domain}.md']=markdown(packet)
    files['docs/SOURCES.md']='# 来源目录\n\n原始文件不在此仓库复制。以下定位用于复查；账号、用户自述、方案文档和助手分析证明力不同。\n\n'+'\n\n'.join(
        f"## {s['id']} · {s['title']}\n\n- 类型：{s['kind']}\n- 来源日期：{s['date']}\n- 定位：{s['locator']}\n- 边界：{s['limitation']}" for s in sources)+'\n'
    lines=['# 时间线','', '按来源中的观察日期排列；日期未知的记录单列。没有把导入日期当作事件发生日期。','']
    for f in sorted(all_facts,key=lambda f:(f['observed_at'] is None,f['observed_at'] or '',f['id'])):
        lines.append(f"- {f['observed_at'] or '日期未知'} · {f['id']} · [{f['status']}] {f['statement']}")
    files['docs/TIMELINE.md']='\n'.join(lines)+'\n'
    for profile in ['general','full','officeflow','engineering','business','english','coding','content','research']:
        packet=envelope(data,select(data,profile,'private',False,as_of),profile,'private',as_of,False)
        files[f'contexts/{profile}.md']=markdown(packet)
    snapshot=[f for f in all_facts if f['id'] in {'ID007','CO016','OF018','OF019','OF021','OF025','OF026','EN001','EN014','LE005','LE006','BU001','DE001','UN003','UN008'}]
    files['CURRENT.md']=markdown(envelope(data,snapshot,'general','private',as_of,False))
    lines=['# 到期复核清单','',f'复核检查日：{as_of.isoformat()}。本文件不触发自动任务；只列出可核对的记录。','']
    for f in all_facts:
        if freshness(f,as_of)=='review_due':lines.append(f"- {f['id']} · {f['observed_at']} · {f['statement']}")
    files['docs/REVIEW_QUEUE.md']='\n'.join(lines)+'\n'
    for path,text in files.items():write(root/path,text)
    manifest={'generated_as_of':as_of.isoformat(),'data_sha256':hashlib.sha256((root/'data/facts.json').read_bytes()).hexdigest(),'files':{k:hashlib.sha256(v.encode()).hexdigest() for k,v in sorted(files.items())}}
    write(root/'data/build-manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return len(files)

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('validate')
    b=sub.add_parser('build');b.add_argument('--as-of',type=parse_date,default=date.today())
    e=sub.add_parser('export');e.add_argument('--profile',choices=PROFILES,default='general')
    e.add_argument('--audience',choices=LEVELS,default='private')
    e.add_argument('--format',choices=['md','json'],default='md')
    e.add_argument('--history',action='store_true');e.add_argument('--as-of',type=parse_date,default=date.today())
    e.add_argument('--output',type=Path);e.add_argument('--max-facts',type=int)
    args=parser.parse_args(argv)
    try:
        data,sources=load()
        problems=errors(data,sources)
        if problems:raise ValueError('\n'.join(problems))
        if args.command=='validate':
            print(f"OK: {len(data['facts'])} facts, {len(sources)} sources");return 0
        if args.command=='build':
            print(f"Built {build(data,sources,args.as_of)} documents");return 0
        facts=select(data,args.profile,args.audience,args.history,args.as_of)
        total=len(facts)
        if args.max_facts is not None:
            if args.max_facts<1:raise ValueError('--max-facts must be positive')
            facts=facts[:args.max_facts]
        packet=envelope(data,facts,args.profile,args.audience,args.as_of,args.history)
        packet['selected_before_limit']=total;packet['omitted_by_limit']=total-len(facts)
        output=json.dumps(packet,ensure_ascii=False,indent=2)+'\n' if args.format=='json' else markdown(packet)+f'\n导出条数：{len(facts)}；因条数限制省略：{total-len(facts)}。\n'
        if args.output:write(args.output.resolve(),output)
        else:print(output,end='')
        return 0
    except (ValueError,TypeError,KeyError,OSError) as exc:
        print('ERROR: '+str(exc),file=sys.stderr);return 1

if __name__=='__main__':sys.exit(main())
