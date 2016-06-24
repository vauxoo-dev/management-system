<<<<<<< a235f9511a527a31b4f2a7a2a68f45c3463732e0
=======
# -*- coding: utf-8 -*-

from openerp import exceptions
>>>>>>> Improving test coverage
from openerp.tests import common


class TestModelAction(common.TransactionCase):
    def test_create_action(self):
        record = self.env['mgmtsystem.action'].create({
            "name": "SampleAction",
<<<<<<< 1b8e49b877d1f53e685156cb680857f6d57d1f8c
            "type_action": "immediate",
=======
            "type_action": "immediate"
>>>>>>> Fixing test error
        })

        self.assertEqual(record.name, "SampleAction")
        self.assertNotEqual(record.reference, "NEW")
        self.assertEqual(record.type_action, "immediate")
        self.assertEqual(record.stage_id.name, "Draft")
        self.assertEqual(record.stage_id.is_starting, True)

    def test_case_open(self):
<<<<<<< f6b774890daa11142d5dd0f33efc18252f456ac9
<<<<<<< 30b7755499fb1bc52d6afb3c3e19c803eb3ba928
=======
=======
        """Test object open state."""
>>>>>>> Fixing error by making test work
        record = self.env['mgmtsystem.action'].create({
            "name": "SampleAction",
            "type_action": "immediate",
        })

        record.write(
            {'active': False, 'stage_id': record._get_stage_open().id})

        ret = record.case_open()

        self.assertEqual(ret, True)
        self.assertEqual(record.active, True)
        self.assertEqual(record.stage_id.name, 'In Progress')
        self.assertEqual(record.stage_id.is_starting, False)
        self.assertEqual(record.stage_id.is_ending, False)

    def test_get_new_stage(self):
        """Get stage new."""
        record = self.env['mgmtsystem.action'].create({
            "name": "SampleAction",
            "type_action": "immediate",
        })
        stage = record._get_stage_new()

        self.assertEqual(stage.name, 'Draft')

    def test_case_close(self):
        """Test object close state."""
<<<<<<< a235f9511a527a31b4f2a7a2a68f45c3463732e0
        stage = self.env.ref('mgmtsystem_action.stage_close')
>>>>>>> add the case_open method, because it is usefull for mgmtsystem_nonconformity
=======
>>>>>>> Improving test coverage
        record = self.env['mgmtsystem.action'].create({
            "name": "SampleAction",
            "type_action": "immediate",
        })
<<<<<<< a235f9511a527a31b4f2a7a2a68f45c3463732e0

        record.active = False

        ret = record.case_open()

        self.assertEqual(ret, True)
        self.assertEqual(record.active, True)
        self.assertEqual(record.stage_id.name, 'In Progress')
        self.assertEqual(record.stage_id.is_starting, False)
        self.assertEqual(record.stage_id.is_ending, False)
=======
        stage = record._get_stage_open()
        stage_new = record._get_stage_new()
        record.stage_id = stage
        stage = record._get_stage_close()
        record.stage_id = stage
        self.assertEqual(record.date_closed[:-3], datetime.now().strftime(
            '%Y-%m-%d %H:%M'
        ))
        try:
            record.write({'stage_id': stage_new.id})
        except exceptions.ValidationError:
            self.assertTrue(True)
        stage = record._get_stage_cancel()
        record.stage_id = stage
        self.assertFalse(record.date_closed)
        self.assertFalse(record.opening_date)
        stage = record._get_stage_close()
        try:
            record.write({'stage_id': stage.id})
        except exceptions.ValidationError:
            self.assertTrue(True)
>>>>>>> Improving test coverage

    def test_get_action_url(self):
        record = self.env['mgmtsystem.action'].create({
            "name": "SampleAction",
            "type_action": "immediate",
        })

        ret = record.get_action_url()

        self.assertEqual(isinstance(ret, list), True)
        self.assertEqual(len(ret), 1)
        self.assertEqual(isinstance(ret[0], basestring), True)
        self.assertEqual(ret[0].startswith('http'), True)
