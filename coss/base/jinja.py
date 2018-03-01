import jinja2
from jinja2.ext import Extension
from wagtailmenus.templatetags.menu_tags import main_menu, sub_menu


class MenuExtension(Extension):

    def __init__(self, environment):
        """Update the environment to include `main_menu` and `sub_menu`
        from the wagtailmenus library.
        """

        super().__init__(environment)
        environment.globals.update({
            'main_menu': jinja2.contextfunction(main_menu),
            'sub_menu': jinja2.contextfunction(sub_menu)
        })
