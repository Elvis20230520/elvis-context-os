import copy
import importlib.util
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

spec=importlib.util.spec_from_file_location('context',Path(__file__).resolve().parents[1]/'scripts/context.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)

class ContextTests(unittest.TestCase):
    def setUp(self):self.data,self.sources=c.load();self.when=date(2026,10,20)
    def test_seed_valid(self):self.assertEqual(c.errors(self.data,self.sources),[])
    def test_public_default_deny(self):self.assertEqual(c.select(self.data,'full','public',as_of=self.when),[])
    def test_no_finance_in_private(self):
        facts=c.select(self.data,'full','private',as_of=self.when)
        self.assertTrue(facts);self.assertFalse(any(f['sensitivity']=='restricted' for f in facts))
    def test_public_export_no_private_source_locators(self):
        d=copy.deepcopy(self.data);d['facts'][0].update(sensitivity='public',public_approved=True)
        facts=c.select(d,'full','public',as_of=self.when)
        self.assertEqual(len(facts),1);self.assertNotIn('sources',facts[0])
    def test_classification_alone_not_public_approval(self):
        d=copy.deepcopy(self.data);d['facts'][0]['sensitivity']='public'
        self.assertEqual(c.select(d,'full','public',as_of=self.when),[])
    def test_history_not_relabelled_current(self):
        f=next(f for f in c.select(self.data,'full','restricted',as_of=self.when) if f['id']=='FI001')
        self.assertEqual(f['status'],'historical');self.assertEqual(f['observed_at'],'2025-11-01')
    def test_missing_source_duplicate_id_invalid(self):
        d=copy.deepcopy(self.data);d['facts'][0]['sources']=['MISSING'];d['facts'].append(d['facts'][0])
        self.assertTrue(any('unresolved' in s for s in c.errors(d,self.sources)))
        self.assertTrue(any('duplicate' in s for s in c.errors(d,self.sources)))
    def test_replacement_hidden_even_if_new_fact_filtered(self):
        d=copy.deepcopy(self.data);old=d['facts'][0];old['status']='superseded'
        new=copy.deepcopy(old);new.update(id='ID999',sensitivity='restricted',status='current',supersedes=[old['id']])
        d['facts'].append(new)
        self.assertNotIn(old['id'],[f['id'] for f in c.select(d,'full','private',as_of=self.when)])
    def test_cycle_invalid(self):
        d=copy.deepcopy(self.data);a,b=d['facts'][:2];a['status']=b['status']='superseded'
        a['supersedes']=[b['id']];b['supersedes']=[a['id']]
        self.assertIn('supersedes cycle',c.errors(d,self.sources))
    def test_bad_date_and_unknown_field(self):
        d=copy.deepcopy(self.data);d['facts'][0].update(observed_at='yesterday',made_up=True)
        self.assertTrue(c.errors(d,self.sources))
    def test_future_review_due(self):
        f=next(f for f in self.data['facts'] if f['id']=='OF021')
        self.assertEqual(c.freshness(f,date(2026,12,31)),'review_due')
    def test_build_deterministic_and_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'data').mkdir();(root/'data/facts.json').write_text(json.dumps(self.data))
            count=c.build(self.data,self.sources,self.when,root)
            before=(root/'data/build-manifest.json').read_bytes()
            self.assertGreater(count,20);c.build(self.data,self.sources,self.when,root)
            self.assertEqual(before,(root/'data/build-manifest.json').read_bytes())
    def test_project_profile_scope(self):
        facts=c.select(self.data,'engineering','private',as_of=self.when)
        self.assertTrue(any(f['domain']=='engineering' for f in facts))
        self.assertFalse(any(f['domain'] in {'finance','devices','research'} for f in facts))

if __name__=='__main__':unittest.main()
