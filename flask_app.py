from flask import Flask, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_session import Session

import pandas as pd
import numpy as np
from datetime import date

import forms as f

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SESSION_TYPE'] = 'filesystem'
bootstrap = Bootstrap(app)
Session(app)


def extract_player_data(form, players, player_idx):
    player_data = []
    prefix = f'player{player_idx}'
    for field_name, value in form.data.items():
        if field_name.startswith(prefix):
            player_data.append(value)

    throws_sum = sum(player_data)
    row = player_data + [throws_sum, players[player_idx], ''.join(sorted(players)), date.today()]
    return row


def forms_dispatcher(n_players):
    forms_dict = {1: f.FormOnePlayer(),
                  2: f.FormTwoPlayers(),
                  3: f.FormThreePlayers(),
                  4: f.FormFourPlayers()}
    return forms_dict[n_players]


@app.route('/', methods=['GET', 'POST'])
def index():
    session['key'] = 'hard to guess string'
    form = f.PlayersForm()

    if form.validate_on_submit():
        players = []
        for field_name, value in form.data.items():
            if field_name.startswith('player') and value != 'None':
                players.append(value)
        np.random.shuffle(players)
        session['players'] = players
        return redirect(url_for('game'))

    return render_template('index.html',
                           form=form)


@app.route('/game', methods=['GET', 'POST'])
def game():
    players = session['players']
    n_players = len(players)
    form = forms_dispatcher(n_players)

    df = pd.read_csv('darts_data/df.csv')
    idx = df.shape[0]

    if form.validate_on_submit():
        for i in range(len(players)):
            row = extract_player_data(form, players, i)
            df.loc[idx+i] = row

        df.to_csv('darts_data/df.csv', index=False)
        return redirect(url_for('game'))

    data = df[df['date'] == str(date.today())]

    data = data[data['players'] == ''.join(sorted(players))]
    players_data = np.array([data[data['player'] == player]['sum'] for player in players])
    players_data = np.transpose(players_data)
    players_data = np.flip(players_data, axis=0)

    max_score = np.max(players_data, axis=1)
    players_with_score = [player + f', {np.sum(players_data[:, idx] == max_score)}'
                          for idx, player in enumerate(players)]
    return render_template('game.html',
                           form=form,
                           players=players_with_score,
                           players_data=players_data)

