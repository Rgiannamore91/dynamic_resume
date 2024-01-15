from flask_wtf import FlaskForm
from flask_wtf.file import  FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, RadioField, IntegerField, FieldList
from wtforms.validators import DataRequired, NumberRange, Regexp, Email

class UpdatePhotoForm(FlaskForm):
    photo = FileField('Update Photo', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Wrong File Type!')])
    submit = SubmitField('Update Photo')

class UpdateHeadlineForm(FlaskForm):
    n_val = IntegerField('How many?', validators=[DataRequired(), NumberRange(min=1)])
    vals = FieldList(StringField('Value', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField("Update")

class UpdatePhoneNumberForm(FlaskForm):
    phone_number = StringField('Phone Number', 
                               validators=[DataRequired(), 
                                Regexp('^\\+1\\s\\d{3}-\\d{3}-\\d{4}$', 
                                message='Enter Phone Number')])
    submit = SubmitField("Update")

class UpdateEmailForm(FlaskForm):
    email = StringField('Email Address', 
                        validators=[DataRequired(), 
                                    Email()])
    submit = SubmitField("Update")

class UpdateLocationForm(FlaskForm):
    location = StringField('Location', 
                           validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateSummaryForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateProgrammingLanguages(FlaskForm):
    submit = SubmitField("Update")

class UpdateFrameworkForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateSoftTechForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateCompetenciesForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateSoftSkillsForm(FlaskForm):
    submit = SubmitField("Update")

class UpdadeRelevantExperienceForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateTempExperienceForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateOtherExperienceForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateDegreeProgramsForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateCertificateProgramsForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateLinksForm(FlaskForm):
    submit = SubmitField("Update")

class UpdateCertificatesForm(FlaskForm):
    submit = SubmitField("Update")

class UpdatePortfolioForm(FlaskForm):
    submit = SubmitField("Update")


