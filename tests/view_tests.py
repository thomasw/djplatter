from django.test.client import RequestFactory
from mock import patch
from unittest2 import TestCase

from djplatter.views import ServeTemplates


class ServeTemplatesInstantiation(TestCase):
    def setUp(self):
        self.bad_st_cbgv = type('TemplateServer', (ServeTemplates,), {})
        self.good_st_cbgv = type('TemplateServer', (ServeTemplates,), {
            'template_dir': '/my/template/dir/'
        })

    def test_fails_if_no_template_dir_is_set_on_cbgv(self):
        """fails if no template_dir is set on cbgv"""
        self.assertRaises(AssertionError, self.bad_st_cbgv)

    def test_succeeds_if_template_dir_is_set(self):
        """"succeeds if template_dir is set on cbgv"""
        self.assertIsInstance(self.good_st_cbgv(), ServeTemplates)


class ServeTemplatesAsView(TestCase):
    def setUp(self):
        content_collection_patcher = patch('djplatter.views.ContentCollection')
        self.content_collection_mock = content_collection_patcher.start()
        self.content_collection = self.content_collection_mock.return_value
        self.content_collection.select.return_value = '/a/template.html'
        self.addCleanup(content_collection_patcher.stop)

        render_patcher = patch('djplatter.views.render')
        self.render_mock = render_patcher.start()
        self.addCleanup(render_patcher.stop)

        self.my_st_cbgv = type('TemplateServer', (ServeTemplates,), {
            'template_dir': '/template/dir/'
        })
        self.view = self.my_st_cbgv.as_view()
        self.request = RequestFactory().get('/some/path/')
        self.response = self.view(self.request, path='/path/')

    def test_instantiates_a_content_collection(self):
        self.content_collection_mock.assert_called_once_with('/template/dir/')

    def test_selects_a_template_from_a_content_collection(self):
        self.content_collection.select.assert_called_once_with(
            self.request, '/path/')

    def test_renders_the_selected_template(self):
        self.render_mock.assert_called_once_with(
            self.request, '/a/template.html')
