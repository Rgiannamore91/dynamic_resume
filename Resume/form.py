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
    summary = TextAreaField('Summary', validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateProgrammingLanguages(FlaskForm):
    p_language = StringField("Programming Language", validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateFrameworkForm(FlaskForm):
    framework = StringField("Framework", validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateSoftTechForm(FlaskForm):
    soft_tech = StringField("Software/Technology", validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateCompetenciesForm(FlaskForm):
    competency = StringField("Competency", validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateSoftSkillsForm(FlaskForm):
    soft_skills = StringField('Soft Skill', validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdadeRelevantExperienceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    tenure = StringField('Tenure', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateTempExperienceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    tenure = StringField('Tenure', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateOtherExperienceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    tenure = StringField('Tenure', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateDegreeProgramsForm(FlaskForm):
    school = StringField('School', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    field = StringField('Field', validators=[DataRequired()])
    period = StringField('Period', validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateCertificateProgramsForm(FlaskForm):
    school = StringField('School', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    field = StringField('Field', validators=[DataRequired()])
    period = StringField('Period', validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateLinksForm(FlaskForm):
    link = StringField('Link', validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdateCertificatesForm(FlaskForm):
    cert = StringField('Certification', validators=[DataRequired()])
    submit = SubmitField("Update")

class UpdatePortfolioForm(FlaskForm):
    p_item = StringField('Portfolio Item', validators=[DataRequired()])
    submit = SubmitField("Update")


