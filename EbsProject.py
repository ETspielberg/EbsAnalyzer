class EbsProject:

    @property
    def project_id(self):
        return self._project_id

    @property
    def filename(self):
        return self._filename

    @property
    def mode(self):
        return self._mode

    @property
    def limit(self):
        return self._limit

    @property
    def available_limit(self):
        return self._available_limit

    @project_id.setter
    def project_id(self, project_id):
        self._project_id = project_id

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    @mode.setter
    def mode(self, mode):
        self._mode = mode

    @limit.setter
    def limit(self, limit):
        self._limit = limit
        self._available_limit = limit

    @available_limit.setter
    def available_limit(self, available_limit):
        self._available_limit = available_limit

    def __init__(self, project_id, filename, mode='price_normalized_percentiles', limit=10000, available_limit=None):
        self._project_id = project_id
        self._filename = filename
        self._mode = mode
        self._limit = limit
        if available_limit is None:
            self._available_limit = limit
        else:
            self._available_limit = available_limit

    def remove_costs_for_fixed(self, cost_fixed):
        self._available_limit -= cost_fixed

    def __getstate__(self):
        state = self.__dict__.copy()
        return {k.lstrip('_'): v for k, v in state.items()}
