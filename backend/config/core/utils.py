
from django.http import JsonResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.utils import timezone
import datetime
from re import sub




def convert_to_snake_case(s):
  if not s:
      return None
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()


def give_form_json_error(errors):
    try:
        msg = list(errors.as_data()["__all__"][0])
        return msg[0]
    except:
        return errors

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def convert_keys_to_camel_case(input_dict):
    if not isinstance(input_dict, dict):
        return input_dict

    camel_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            camel_dict[snake_to_camel(key)] = convert_keys_to_camel_case(value)
        elif isinstance(value, list):
            camel_dict[snake_to_camel(key)] = [convert_keys_to_camel_case(item) for item in value]
        else:
            camel_dict[snake_to_camel(key)] = value

    return camel_dict

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return HttpResponse("Error")



def give_formatted_date_time(date_t):
    try:
        if not date_t:
            return None
        tz = timezone.get_default_timezone()
        value = timezone.localtime(date_t, timezone=tz)
        return value.strftime("%Y-%m-%d %I:%M %p")
    except:
        return None
    




def get_time_interval_with_break(start_time:datetime.time,end_time,interval,break_start_time=None, break_end_time=None):
    time_ranges = []
    interval = datetime.timedelta(minutes=interval)
    current_time = start_time

    while current_time < end_time:
        next_time = (datetime.datetime.combine(datetime.date.today(), current_time) + interval).time()
        if break_start_time and break_end_time:
            if break_start_time <= current_time < break_end_time:
                current_time = break_end_time
                continue
            elif current_time < break_start_time <= next_time:
                time_ranges.append((current_time, break_start_time))
                current_time = break_end_time
                continue
        else:
            time_ranges.append((current_time, next_time))
            current_time = next_time
    return time_ranges


def filter_range_from_time(for_date, time_list, policy_time_to_check):
    filtered_time_list = []
    for time_str in time_list:
        time_obj=time_str[0]
        n_date = datetime.datetime.combine(for_date, time_obj)
        if n_date > policy_time_to_check:
            filtered_time_list.append((time_str))
    return filtered_time_list


def get_date_between_range(start_date,end_date):
    date_list = []  
    for n in range(int((end_date - start_date).days) + 1):
        date_list.append(start_date + datetime.timedelta(n))

    return date_list
