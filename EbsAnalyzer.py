import math
from statistics import mean
import numpy as np

available_models = [
    'only_usage',
    'only_cost_per_usage',
    'price_normalized_percentiles',
    'percentage_normalized_percentiles',
    'usage_normalized_percentiles',
    'index',
    'index_weighting',
    'value_weighting',
    'index_weighting_exponential'
    'value_weighting_exponential'
]


def combine_selections(selection_one, selection_two):
    return selection_one and selection_two


def set_bools_usage_for_cost_limit(ebs_titles, cost_limit):
    total_sum = 0
    ebs_titles.sort_values('Total', ascending=False, inplace=True)
    selection = []
    for index, title in ebs_titles.iterrows():
        total_sum += title['Preis']
        selection.append(total_sum < cost_limit)
    ebs_titles['Auswahl Nutzung'] = np.array(selection)
    return ebs_titles


def set_bools_cost_per_usage_for_cost_limit(ebs_titles, cost_limit):
    total_sum = 0
    ebs_titles.sort_values('Kosten pro Nutzung', ascending=True, inplace=True)
    selection = []
    for index, title in ebs_titles.iterrows():
        total_sum += title['Preis']
        selection.append(total_sum < cost_limit)
    ebs_titles['Auswahl Kosten pro Nutzung'] = np.array(selection)
    return ebs_titles


def set_bools_usage_for_usage_limit(ebs_titles, usage_limit):
    total_sum = 0
    ebs_titles.sort_values('Total', ascending=False, inplace=True)
    for index, title in ebs_titles.iterrows():
        total_sum += title['Total']
        ebs_titles['Auswahl Nutzung'] = total_sum < usage_limit
    return ebs_titles


def set_bools_cost_per_usage_for_usage_limit(ebs_titles, usage_limit):
    total_sum = 0
    ebs_titles.sort_values('Kosten pro Nutzung', ascending=True, inplace=True)
    selection = []
    for index, title in ebs_titles.iterrows():
        total_sum += title['Total']
        selection.append(total_sum < usage_limit)
    ebs_titles['Auswahl Nutzung'] = (total_sum < usage_limit)
    return ebs_titles


def set_position_for_usage(ebs_titles):
    ebs_titles.sort_values('Total', ascending=False, inplace=True)
    weighting_index = 0
    weighting_indices = []
    for index, title in ebs_titles.iterrows():
        weighting_index += index
        weighting_indices.append(weighting_index)
    ebs_titles['Wichtungsfaktor'] = np.array(weighting_indices)
    return ebs_titles


def set_position_for_cost_per_usage(ebs_titles):
    weighting_index = 0
    weighting_indices = []
    ebs_titles.sort_values('Kosten pro Nutzung', ascending=True, inplace=True)
    for index, title in ebs_titles.iterrows():
        weighting_index += index
        weighting_indices.append(weighting_index)
    ebs_titles['Wichtungsfaktor'] = np.array(weighting_indices)
    return ebs_titles


def set_weighting_for_usage(ebs_titles):
    max_usage = ebs_titles['Total'].max()
    ebs_titles['Wichtungsfaktor'] = [x * y / max_usage for x, y in
                                     zip(ebs_titles['Wichtungsfaktor'], ebs_titles['Total'])]
    return ebs_titles


def set_weighting_for_cost_per_usage(ebs_titles):
    max_cost_per_usage = ebs_titles['Kosten pro Nutzung'].min()
    ebs_titles['Wichtungsfaktor'] = [x * (max_cost_per_usage - y) / max_cost_per_usage for x, y in
                                     zip(ebs_titles['Wichtungsfaktor'], ebs_titles['Kosten pro Nutzung'])]
    return ebs_titles


def set_weighting_for_position_usage(ebs_titles):
    ebs_titles.sort_values('Total', ascending=False, inplace=True)
    weighting_indices = []
    for index, title in ebs_titles.iterrows():
        weighting_indices.append(title['Wichtungsfaktor'] * (index - 1) / len(ebs_titles))
    ebs_titles['Wichtungsfaktor'] = np.array(weighting_indices)
    return ebs_titles


def set_weighting_for_position_cost_per_usage(ebs_titles):
    ebs_titles.sort_values('Kosten pro Nutzung', ascending=True, inplace=True)
    weighting_indices = []
    for index, title in ebs_titles.iterrows():
        weighting_indices.append(title['Wichtungsfaktor'] * (index - 1) / len(ebs_titles))
    ebs_titles['Wichtungsfaktor'] = np.array(weighting_indices)
    return ebs_titles


def set_exponential_weighting_for_usage(ebs_titles):
    mean_usage = ebs_titles['Total'].mean()
    ebs_titles['Wichtungsfaktor'] = [x * math.exp((float(y - mean_usage)) / mean_usage) for x, y in
                                     zip(ebs_titles['Wichtungsfaktor'], ebs_titles['Total'])]
    return ebs_titles


def set_exponential_weighting_for_cost_per_usage(ebs_titles):
    mean_cost_per_usage = mean(title.cost_per_usage for title in ebs_titles)
    ebs_titles['Wichtungsfaktor'] = [x * math.exp(y / mean_cost_per_usage) for x, y in
                                     zip(ebs_titles['Wichtungsfaktor'], ebs_titles['Kosten pro Nutzung'])]
    return ebs_titles


def set_exponential_weighting_for_position_usage(ebs_titles):
    ebs_titles.sort_values('Total', ascending=False, inplace=True)
    weighting_indices = []
    for index, title in ebs_titles.iterrows():
        weighting_indices.append(title['Wichtungsfaktor'] * math.exp(-float(index - 1) / len(ebs_titles)))
    ebs_titles['Wichtungsfaktor'] = np.array(weighting_indices)
    return ebs_titles


def set_exponential_weighting_for_position_cost_per_usage(ebs_titles):
    ebs_titles.sort_values('Kosten pro Nutzung')
    weighting_indices = []
    for index, title in ebs_titles.iterrows():
        weighting_indices.append(title['Wichtungsfaktor'] * math.exp(-float(index - 1) / len(ebs_titles)))
    ebs_titles['Wichtungsfaktor'] = np.array(weighting_indices)
    return ebs_titles


def make_selection_for_usage_with_threshold(ebs_titles, threshold):
    total_sum = 0
    ebs_titles.sort_values('Total', ascending=False, inplace=True)
    selection = []
    for index, title in ebs_titles.iterrows():
        if index < threshold:
            selection.append(True)
            total_sum += title['Preis']
        else:
            selection.append(False)
    ebs_titles['Auswahl Nutzung'] = np.array(selection)
    return ebs_titles, total_sum


def make_selection_for_cost_per_usage_with_threshold(ebs_titles, threshold):
    total_sum = 0
    ebs_titles.sort_values('Kosten pro Nutzung', ascending=True, inplace=True)
    selection = []
    for index, title in ebs_titles.iterrows():

        if index < threshold:
            selection.append(True)
            total_sum += title['Preis']
        else:
            selection.append(False)
    ebs_titles['Auswahl Kosten pro Nutzung'] = np.array(selection)
    return ebs_titles, total_sum


def get_price_for_selection(ebs_titles):
    total_sum = 0
    for index, title in ebs_titles.iterrows():
        if title['Auswahl']:
            total_sum += title['Preis']
    return ebs_titles, total_sum


def get_price_for_list_with_weighting(ebs_titles, limit):
    total_sum = 0
    ebs_titles.sort_values('Wichtungsfaktor')
    selection = []
    for index, title in ebs_titles.iterrows():
        if total_sum < limit:
            total_sum += title['Preis']
            selection.append(True)
        else:
            selection.append(False)
    ebs_titles['Auswahl'] = np.array(selection)
    return ebs_titles, total_sum


class EbsAnalyzer(object):

    def __init__(self, ebs_mode):
        self._method = getattr(self, ebs_mode, lambda: 0)

    def make_selection(self, ebs_limit, ebs_titles):
        return self._method(ebs_limit=ebs_limit, ebs_titles=ebs_titles)

    def only_usage(self, ebs_limit, ebs_titles):
        ebs_titles = set_bools_usage_for_cost_limit(ebs_titles, ebs_limit)
        ebs_titles['Auswahl'] = ebs_titles['Auswahl Nutzung']
        return get_price_for_selection(ebs_titles)

    def only_cost_per_usage(self, ebs_limit, ebs_titles):
        ebs_titles = set_bools_cost_per_usage_for_cost_limit(ebs_titles, ebs_limit)
        ebs_titles['Auswahl'] = ebs_titles['Auswahl Kosten pro Nutzung']
        return get_price_for_selection(ebs_titles)

    def price_normalized_percentiles(self, ebs_titles, ebs_limit):
        virtual_limit = 1.5 * ebs_limit
        ebs_titles = set_bools_usage_for_cost_limit(ebs_titles, virtual_limit)
        ebs_titles = set_bools_cost_per_usage_for_cost_limit(ebs_titles, virtual_limit)
        ebs_titles['Auswahl'] = np.vectorize(combine_selections)(ebs_titles['Auswahl Nutzung'],
                                                                 ebs_titles['Auswahl Kosten pro Nutzung'])
        ebs_titles, sum_selected = get_price_for_selection(ebs_titles)
        step_differ = True
        n_cycles = 0
        while step_differ:
            n_cycles += 1
            difference = sum_selected - ebs_limit
            virtual_limit -= difference * 0.8
            old_selected_sum = sum_selected
            ebs_titles = set_bools_usage_for_cost_limit(ebs_titles, virtual_limit)
            ebs_titles = set_bools_cost_per_usage_for_cost_limit(ebs_titles, virtual_limit)
            ebs_titles['Auswahl'] = np.vectorize(combine_selections)(ebs_titles['Auswahl Nutzung'],
                                                                     ebs_titles['Auswahl Kosten pro Nutzung'])
            ebs_titles, sum_selected = get_price_for_selection(ebs_titles)
            if (sum_selected - old_selected_sum) == 0:
                step_differ = False
            if n_cycles == 100:
                step_differ = False
        return ebs_titles, sum_selected

    def percentage_normalized_percentiles(self, ebs_titles, ebs_limit):
        mean_price = mean(title['Preis'] for index, title in ebs_titles.iterrows())
        number = ebs_limit // mean_price
        ebs_titles, total_sum = make_selection_for_usage_with_threshold(ebs_titles, number)
        ebs_titles, total_sum = make_selection_for_cost_per_usage_with_threshold(ebs_titles, number)
        ebs_titles['Auswahl'] = np.vectorize(combine_selections)(ebs_titles['Auswahl Nutzung'],
                                                                 ebs_titles['Auswahl Kosten pro Nutzung'])
        ebs_titles, price_selected = get_price_for_selection(ebs_titles)
        step_differ = True
        n_cycles = 0
        while step_differ:
            n_cycles += 1
            old_selected_sum = price_selected
            if price_selected != 0:
                fraction = float((price_selected - ebs_limit)) / float(price_selected)
            else:
                fraction = 2
            number = number * (1 - fraction)
            ebs_titles, total_sum = make_selection_for_usage_with_threshold(ebs_titles, int(number))
            ebs_titles, total_sum = make_selection_for_cost_per_usage_with_threshold(ebs_titles, int(number))
            ebs_titles['Auswahl'] = np.vectorize(combine_selections)(ebs_titles['Auswahl Nutzung'],
                                                                     ebs_titles['Auswahl Kosten pro Nutzung'])
            ebs_titles, sum_selected = get_price_for_selection(ebs_titles)
            if (sum_selected - old_selected_sum) == 0:
                step_differ = False
            if n_cycles == 100:
                step_differ = False
        return ebs_titles, price_selected

    def usage_normalized_percentiles(self, ebs_titles, ebs_limit):
        mean_usage = mean(title['Total'] for index, title in ebs_titles.iterrows())
        mean_price = mean(title['Preis'] for index, title in ebs_titles.iterrows())
        usage_threshold = int(ebs_limit / mean_price * mean_usage)
        set_bools_usage_for_usage_limit(ebs_titles, usage_threshold)
        set_bools_cost_per_usage_for_usage_limit(ebs_titles, usage_threshold)
        ebs_titles, price_selected = get_price_for_selection(ebs_titles)
        step_differ = True
        n_cycles = 0
        while step_differ:
            n_cycles += 1
            old_selected_sum = price_selected
            if price_selected != 0:
                fraction = float((price_selected - ebs_limit)) / (8 * ebs_limit)
            else:
                fraction = 2
            usage_threshold = usage_threshold * (1 - fraction)
            set_bools_usage_for_usage_limit(ebs_titles, usage_threshold)
            set_bools_cost_per_usage_for_usage_limit(ebs_titles, usage_threshold)
            ebs_titles, price_selected = get_price_for_selection(ebs_titles)
            print(price_selected)
            if (price_selected - old_selected_sum) == 0:
                step_differ = False
            if n_cycles == 100:
                step_differ = False
        return ebs_titles, price_selected

    def index(self, ebs_titles, ebs_limit):
        set_position_for_usage(ebs_titles)
        set_position_for_cost_per_usage(ebs_titles)
        return get_price_for_list_with_weighting(ebs_titles, ebs_limit)

    def index_weighting(self, ebs_titles, ebs_limit):
        set_weighting_for_position_usage(ebs_titles)
        set_weighting_for_position_cost_per_usage(ebs_titles)
        return get_price_for_list_with_weighting(ebs_titles, ebs_limit)

    def value_weighting(self, ebs_titles, ebs_limit):
        set_weighting_for_usage(ebs_titles)
        set_weighting_for_cost_per_usage(ebs_titles)
        return get_price_for_list_with_weighting(ebs_titles, ebs_limit)

    def index_weighting_exponential(self, ebs_titles, ebs_limit):
        set_exponential_weighting_for_position_usage(ebs_titles)
        set_exponential_weighting_for_position_cost_per_usage(ebs_titles)
        return get_price_for_list_with_weighting(ebs_titles, ebs_limit)

    def value_weighting_exponential(self, ebs_titles, ebs_limit):
        set_exponential_weighting_for_usage(ebs_titles)
        set_exponential_weighting_for_cost_per_usage(ebs_titles)
        return get_price_for_list_with_weighting(ebs_titles, ebs_limit)
