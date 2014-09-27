class ContentCollection(object):
    def __init__(self, template_dir, config_file_name='overrides.json',
                 file_types=('.html',), ignore_prefixes=('_',)):
        self.template_dir = template_dir
        self.config_file_name = config_file_name
        self.file_types = file_types
        self.ignore_prefixes = ignore_prefixes

    def get_template_path(self, path, query_params=None):
        path = self._normalize_path(path)

        if self._verify_template_exists(path):
            raise Exception('Template does not exist.')

        return path

    def _normalize_path(self, path):
        return path

    def _verify_template_exists(self, path):
        pass
