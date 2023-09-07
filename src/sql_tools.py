from config.config import engine
import pandas as pd

def get5rand():
    query = list(engine.execute("""
    SELECT q.Quote, c.Name, e.Title, e.Seasons_idSeason
    FROM Quotes as q
    LEFT JOIN  Episodes as e
    ON q.Episodes_idEpisode = e.idEpisode
    LEFT JOIN  Characters as c
    ON q.Characters_idCharacter = c.idCharacter
    ORDER BY RAND() LIMIT 5;
    """))
    return query

def char5(name,cuantas):
    query = list(engine.execute(f"""
    SELECT q.Quote, c.Name, e.Title, e.Seasons_idSeason
    FROM Quotes as q
    LEFT JOIN  Episodes as e
    ON q.Episodes_idEpisode = e.idEpisode
    LEFT JOIN  Characters as c
    ON q.Characters_idCharacter = c.idCharacter
    WHERE Characters_idCharacter IN 
	(SELECT idCharacter FROM Simpsons.Characters WHERE Name = "{name}")
    ORDER BY RAND() LIMIT {cuantas};
    """))
    return query 


def sent_analysis(name):
    query = f"""
     SELECT q.Quote, c.Name, e.Title, e.Seasons_idSeason
    FROM Quotes as q
    LEFT JOIN  Episodes as e
    ON q.Episodes_idEpisode = e.idEpisode
    LEFT JOIN  Characters as c
    ON q.Characters_idCharacter = c.idCharacter
    WHERE Characters_idCharacter IN 
	(SELECT idCharacter FROM Simpsons.Characters WHERE Name = "{name}");
    """
    frases = pd.read_sql_query(query,engine)
    
    #me falta la función de NLP
    return frases.shape()
