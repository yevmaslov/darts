from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class PlayersForm(FlaskForm):
    player1 = SelectField(choices=['None', 'Andrii', 'Anna', 'Dima', 'Evgenii', 'Olya', 'Tanya'])
    player2 = SelectField(choices=['None', 'Andrii', 'Anna', 'Dima', 'Evgenii', 'Olya', 'Tanya'])
    player3 = SelectField(choices=['None', 'Andrii', 'Anna', 'Dima', 'Evgenii', 'Olya', 'Tanya'])
    player4 = SelectField(choices=['None', 'Andrii', 'Anna', 'Dima', 'Evgenii', 'Olya', 'Tanya'])
    submit = SubmitField('Play')


class FormOnePlayer(FlaskForm):
    player0_throw1 = IntegerField(validators=[InputRequired()])
    player0_throw2 = IntegerField(validators=[InputRequired()])
    player0_throw3 = IntegerField(validators=[InputRequired()])
    submit = SubmitField('Submit')


class FormTwoPlayers(FlaskForm):
    player0_throw1 = IntegerField(validators=[InputRequired()])
    player0_throw2 = IntegerField(validators=[InputRequired()])
    player0_throw3 = IntegerField(validators=[InputRequired()])

    player1_throw1 = IntegerField(validators=[InputRequired()])
    player1_throw2 = IntegerField(validators=[InputRequired()])
    player1_throw3 = IntegerField(validators=[InputRequired()])
    submit = SubmitField('Submit')


class FormThreePlayers(FlaskForm):
    player0_throw1 = IntegerField(validators=[InputRequired()])
    player0_throw2 = IntegerField(validators=[InputRequired()])
    player0_throw3 = IntegerField(validators=[InputRequired()])

    player1_throw1 = IntegerField(validators=[InputRequired()])
    player1_throw2 = IntegerField(validators=[InputRequired()])
    player1_throw3 = IntegerField(validators=[InputRequired()])

    player2_throw1 = IntegerField(validators=[InputRequired()])
    player2_throw2 = IntegerField(validators=[InputRequired()])
    player2_throw3 = IntegerField(validators=[InputRequired()])
    submit = SubmitField('Submit')


class FormFourPlayers(FlaskForm):
    player0_throw1 = IntegerField(validators=[InputRequired()])
    player0_throw2 = IntegerField(validators=[InputRequired()])
    player0_throw3 = IntegerField(validators=[InputRequired()])

    player1_throw1 = IntegerField(validators=[InputRequired()])
    player1_throw2 = IntegerField(validators=[InputRequired()])
    player1_throw3 = IntegerField(validators=[InputRequired()])

    player2_throw1 = IntegerField(validators=[InputRequired()])
    player2_throw2 = IntegerField(validators=[InputRequired()])
    player2_throw3 = IntegerField(validators=[InputRequired()])

    player3_throw1 = IntegerField(validators=[InputRequired()])
    player3_throw2 = IntegerField(validators=[InputRequired()])
    player3_throw3 = IntegerField(validators=[InputRequired()])
    submit = SubmitField('Submit')
