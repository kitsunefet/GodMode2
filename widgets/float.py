import wtforms

from base.widget import BaseWidget


class FloatWidget(BaseWidget):
    field = wtforms.FloatField()

    def render_list(self, item):
        value = getattr(item, self.name, None)
        try:
            return round(value, 3)
        except:
            return value
