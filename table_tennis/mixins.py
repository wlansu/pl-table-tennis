"""All custom mixins."""


class FieldCSSMixin(object):
    """Adds custom css classes to form field widgets when needed."""

    def get_form(self, form_class):
        """Return the Form.

        Overloaded in order to add our custom css class to the field widget.

        :param form_class: The form_class of this view.
        :return: Django :class:`ModelForm` instance of a model object.
        """
        form = super(FieldCSSMixin, self).get_form(form_class)
        if form.errors:
            for field in form:
                if field.errors:
                    field.field.widget.attrs.update({"class": "uk-form-danger"})
                else:
                    field.field.widget.attrs.update({"class": "uk-form-success"})

        return form
