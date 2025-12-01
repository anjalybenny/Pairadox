import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from hobby_questionnaire import get_hobby_answers_from_user



hobby_interest_universe = np.arange(0, 1.01, 0.01)
category_universe = np.arange(0, 1.01, 0.01)


def add_hobby_interest(hobby_variable):
    hobby_variable['hate']    = fuzz.trimf(hobby_variable.universe, [0.0, 0.0, 0.25])
    hobby_variable['dislike'] = fuzz.trimf(hobby_variable.universe, [0.0, 0.25, 0.5])
    hobby_variable['neutral'] = fuzz.trimf(hobby_variable.universe, [0.25, 0.5, 0.75])
    hobby_variable['like']    = fuzz.trimf(hobby_variable.universe, [0.5, 0.75, 1.0])
    hobby_variable['love']    = fuzz.trimf(hobby_variable.universe, [0.75, 1.0, 1.0])


def add_category(category_variable):
    """Low / Medium / High membership functions for category score."""
    category_variable['low']    = fuzz.trimf(category_variable.universe, [0.0, 0.0, 0.5])
    category_variable['medium'] = fuzz.trimf(category_variable.universe, [0.0, 0.5, 1.0])
    category_variable['high']   = fuzz.trimf(category_variable.universe, [0.5, 1.0, 1.0])


hiking = ctrl.Antecedent(hobby_interest_universe, 'hiking')
cycling = ctrl.Antecedent(hobby_interest_universe, 'cycling')
skiing = ctrl.Antecedent(hobby_interest_universe, 'skiing')
gardening = ctrl.Antecedent(hobby_interest_universe, 'gardening')
walking = ctrl.Antecedent(hobby_interest_universe, 'walking')
fitness = ctrl.Antecedent(hobby_interest_universe, 'fitness')
swimming = ctrl.Antecedent(hobby_interest_universe, 'swimming')
listening_music = ctrl.Antecedent(hobby_interest_universe, 'listening_music')
reading = ctrl.Antecedent(hobby_interest_universe, 'reading')
watching_films_or_series = ctrl.Antecedent(hobby_interest_universe, 'watching_films_or_series')
photography = ctrl.Antecedent(hobby_interest_universe, 'photography')
cooking = ctrl.Antecedent(hobby_interest_universe, 'cooking')
eating_out = ctrl.Antecedent(hobby_interest_universe, 'eating_out')
volunteering = ctrl.Antecedent(hobby_interest_universe, 'volunteering')
travel_switzerland = ctrl.Antecedent(hobby_interest_universe, 'travel_switzerland')
travel_abroad = ctrl.Antecedent(hobby_interest_universe, 'travel_abroad')
social_media = ctrl.Antecedent(hobby_interest_universe, 'social_media')
video_games = ctrl.Antecedent(hobby_interest_universe, 'video_games')
crafting_diy = ctrl.Antecedent(hobby_interest_universe, 'crafting_diy')
learning_languages = ctrl.Antecedent(hobby_interest_universe, 'learning_languages')
continuing_education = ctrl.Antecedent(hobby_interest_universe, 'continuing_education')
meditation = ctrl.Antecedent(hobby_interest_universe, 'meditation')
yoga = ctrl.Antecedent(hobby_interest_universe, 'yoga')
spa_sauna = ctrl.Antecedent(hobby_interest_universe, 'spa_sauna')



for hobby in [
    hiking, cycling, skiing, gardening,
    walking, fitness, swimming,
    listening_music, reading, watching_films_or_series, photography,
    cooking, eating_out, volunteering,
    travel_switzerland, travel_abroad,
    social_media, video_games,
    crafting_diy,
    learning_languages, continuing_education,
    meditation, yoga, spa_sauna
]:
    add_hobby_interest(hobby)



outdoors = ctrl.Consequent(category_universe, 'outdoors')
sports_fitness = ctrl.Consequent(category_universe, 'sports_fitness')
arts_culture = ctrl.Consequent(category_universe, 'arts_culture')
social_lifestyle = ctrl.Consequent(category_universe, 'social_lifestyle')
travel_discovery = ctrl.Consequent(category_universe, 'travel_discovery')
tech_entertainment = ctrl.Consequent(category_universe, 'tech_entertainment')
creative_diy = ctrl.Consequent(category_universe, 'creative_diy')
learning_growth = ctrl.Consequent(category_universe, 'learning_growth')
wellness_mindfulness = ctrl.Consequent(category_universe, 'wellness_mindfulness')


for category in [
    outdoors,
    sports_fitness,
    arts_culture,
    social_lifestyle,
    travel_discovery,
    tech_entertainment,
    creative_diy,
    learning_growth,
    wellness_mindfulness
]:
    add_category(category)



rule_outdoors_high = ctrl.Rule(
    hiking['like'] | hiking['love'] |
    cycling['like'] | cycling['love'] |
    skiing['like'] | skiing['love'] |
    gardening['like'] | gardening['love'],
    outdoors['high']
)

rule_outdoors_low = ctrl.Rule(
    hiking['hate'] &
    cycling['hate'] &
    skiing['hate'] &
    gardening['hate'],
    outdoors['low']
)


rule_sports_high = ctrl.Rule(
    walking['like'] | walking['love'] |
    fitness['like'] | fitness['love'] |
    swimming['like'] | swimming['love'],
    sports_fitness['high']
)

rule_sports_low = ctrl.Rule(
    walking['hate'] &
    fitness['hate'] &
    swimming['hate'],
    sports_fitness['low']
)


rule_arts_high = ctrl.Rule(
    listening_music['like'] | listening_music['love'] |
    reading['like'] | reading['love'] |
    watching_films_or_series['like'] | watching_films_or_series['love'] |
    photography['like'] | photography['love'],
    arts_culture['high']
)

rule_arts_low = ctrl.Rule(
    listening_music['hate'] &
    reading['hate'] &
    watching_films_or_series['hate'] &
    photography['hate'],
    arts_culture['low']
)


rule_social_high = ctrl.Rule(
    cooking['like'] | cooking['love'] |
    eating_out['like'] | eating_out['love'] |
    volunteering['like'] | volunteering['love'],
    social_lifestyle['high']
)

rule_social_low = ctrl.Rule(
    cooking['hate'] &
    eating_out['hate'] &
    volunteering['hate'],
    social_lifestyle['low']
)


rule_travel_high = ctrl.Rule(
    travel_switzerland['like'] | travel_switzerland['love'] |
    travel_abroad['like'] | travel_abroad['love'],
    travel_discovery['high']
)

rule_travel_low = ctrl.Rule(
    travel_switzerland['hate'] &
    travel_abroad['hate'],
    travel_discovery['low']
)

rule_tech_high = ctrl.Rule(
    social_media['like'] | social_media['love'] |
    video_games['like'] | video_games['love'],
    tech_entertainment['high']
)

rule_tech_low = ctrl.Rule(
    social_media['hate'] &
    video_games['hate'],
    tech_entertainment['low']
)

rule_creative_high = ctrl.Rule(
    crafting_diy['like'] | crafting_diy['love'],
    creative_diy['high']
)

rule_creative_low = ctrl.Rule(
    crafting_diy['hate'],
    creative_diy['low']
)

rule_learning_high = ctrl.Rule(
    learning_languages['like'] | learning_languages['love'] |
    continuing_education['like'] | continuing_education['love'],
    learning_growth['high']
)

rule_learning_low = ctrl.Rule(
    learning_languages['hate'] &
    continuing_education['hate'],
    learning_growth['low']
)

rule_wellness_high = ctrl.Rule(
    meditation['like'] | meditation['love'] |
    yoga['like'] | yoga['love'] |
    spa_sauna['like'] | spa_sauna['love'],
    wellness_mindfulness['high']
)

rule_wellness_low = ctrl.Rule(
    meditation['hate'] &
    yoga['hate'] &
    spa_sauna['hate'],
    wellness_mindfulness['low']
)



hobby_ctrl = ctrl.ControlSystem([
    rule_outdoors_high, rule_outdoors_low,
    rule_sports_high, rule_sports_low,
    rule_arts_high, rule_arts_low,
    rule_social_high, rule_social_low,
    rule_travel_high, rule_travel_low,
    rule_tech_high, rule_tech_low,
    rule_creative_high, rule_creative_low,
    rule_learning_high, rule_learning_low,
    rule_wellness_high, rule_wellness_low
])


hobby_sim = ctrl.ControlSystemSimulation(hobby_ctrl)


def map_tuple_to_fuzzy_inputs(answer_tuple):
    fuzzy_variable_names = [
        'hiking',
        'cycling',
        'skiing',
        'gardening',
        'walking',
        'fitness',
        'swimming',
        'listening_music',
        'reading',
        'watching_films_or_series',
        'photography',
        'cooking',
        'eating_out',
        'volunteering',
        'travel_switzerland',
        'travel_abroad',
        'social_media',
        'video_games',
        'crafting_diy',
        'learning_languages',
        'continuing_education',
        'meditation',
        'yoga',
        'spa_sauna'
    ]
    return dict(zip(fuzzy_variable_names, answer_tuple))



def compute_hobby_categories(user):
    for k, v in user.items():
        hobby_sim.input[k] = float(v)

    hobby_sim.compute()

    return {
        'outdoors': float(hobby_sim.output['outdoors']),
        'sports_fitness': float(hobby_sim.output['sports_fitness']),
        'arts_culture': float(hobby_sim.output['arts_culture']),
        'social_lifestyle': float(hobby_sim.output['social_lifestyle']),
        'travel_discovery': float(hobby_sim.output['travel_discovery']),
        'tech_entertainment': float(hobby_sim.output['tech_entertainment']),
        'creative_diy': float(hobby_sim.output['creative_diy']),
        'learning_growth': float(hobby_sim.output['learning_growth']),
        'wellness_mindfulness': float(hobby_sim.output['wellness_mindfulness'])
    }


if __name__ == "__main__":
    raw_answers = get_hobby_answers_from_user()          # tuple
    user_inputs = map_tuple_to_fuzzy_inputs(raw_answers) # dict
    scores = compute_hobby_categories(user_inputs)       # fuzzy system
    print(scores)

