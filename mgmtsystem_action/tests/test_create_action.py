from openerp.tests import common


class TestModelAction(common.TransactionCase):
    def test_create_action(self):
        record = self.env['mgmtsystem.action'].create({
            "name": "SampleAction",
            "type_action": "immediate",
        })

        self.assertEqual(record.name, "SampleAction")
        self.assertNotEqual(record.reference, "NEW")
        self.assertEqual(record.type_action, "immediate")
        self.assertEqual(record.stage_id.name, "Draft")
        self.assertEqual(record.stage_id.is_starting, True)

    def test_case_open(self):
        record = self.env['mgmtsystem.action'].create({
            "name": "SampleAction",
            "type_action": "immediate",
        })

        record.active = False

        ret = record.case_open()

        self.assertEqual(ret, True)
        self.assertEqual(record.active, True)
        self.assertEqual(record.stage_id.name, 'In Progress')
        self.assertEqual(record.stage_id.is_starting, False)
        self.assertEqual(record.stage_id.is_ending, False)

    def test_get_action_url(self):
        record = self.env['mgmtsystem.action'].create({
            "name": "SampleAction",
            "type_action": "immediate",
        })

        url = self.env['ir.config_parameter'].get_param('web.base.url')
        ret = record.get_action_url()

        self.assertIn(url, ret, 'Action link: link should contain web.base.url\
         config parameter.')
        self.assertIn(str(record.id), ret, 'Action link: link should contain\
         record id.')
        self.assertIn(record._model._name, ret, 'Action link: link should\
         contain model name.')
        self.assertEqual(isinstance(ret, basestring), True)
        self.assertEqual(ret.startswith('http'), True)
