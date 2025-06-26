import persistence.UserHistoryPersistence as userHistoryDB
from datetime import datetime, timedelta
import jsonpickle
import dto.UserHistory as uh
import dto.Recipe as recipe


def get_custom_dates(DataJson):
    """
    Estrae da un json la data di inizio e fine.

    Args : 
    - DataJson : stringa JSON 

    Returns : 
    - begin_date, end_date : i campi data di inzio e fine codificati nella stringa JSON in input
    """

    Data = jsonpickle.decode(DataJson)

    begin_date = datetime.strptime(Data["begin_date"]+ " 00:00:00", '%d-%m-%Y %H:%M:%S')
    end_date = datetime.strptime(Data["end_date"]+ " 23:59:59", '%d-%m-%Y %H:%M:%S')
    
    return begin_date, end_date


def get_user_history_of_custom_date(userId, begin_date, end_date, onlyAccepted = True):
    """
    Recupera dalla collection users_food_history del db la cronologia dei suggerimenti alimenatri dell'utente 
    con dato userId del dato intervallo temporale, delimitato dal giormo di inizio e fine.

    Args : 
    - userId : id dell'utente di cui recuperare la cronologia.
    - onlyAccepted : flag booleana che indica se recuperare solo i suggerimenti accettati (di default True)
    - begin_date : giorno di inizio di cui tenere in considerazione la cronologia, nel formato %Y-%m-%d %H:%M:%S.
    - end_date : giorno di fine di cui tenere in considerazione la cronologia, nel formato %Y-%m-%d %H:%M:%S.

    Returns : 
    - userHistory : cronologia dell'ultima settimana dell'utente con dato userId recuperata dal db.
    """
    
    fullUserHistory = userHistoryDB.get_user_history(userId)

    userHistory = []
    for history in fullUserHistory:
        date = datetime.strptime(history['date'], '%Y-%m-%d %H:%M:%S')
        if date >= begin_date and date <= end_date and (not onlyAccepted or history['status'] == 'accepted'or history['status'] == 'asserted'):
            userHistory.append(history)

    if len(userHistory) == 0:
        return None
    
    return userHistory



def get_user_history_of_week(userId, onlyAccepted = True):
    """
    Recupera dalla collection users_food_history del db la cronologia dei suggerimenti alimenatri dell'utente 
    con dato userId dell'ultima settimana.

    Args : 
    - userId : id dell'utente di cui recuperare la cronologia.
    - onlyAccepted : flag booleana che indica se recuperare solo i suggerimenti accettati (di default True)

    Returns : 
    - userHistory : cronologia dell'ultima settimana dell'utente con dato userId recuperata dal db.
    """

    fullUserHistory = userHistoryDB.get_user_history(userId)

    #filter the user history of the week
    sysdate = datetime.today()
    previousWeek = sysdate - timedelta(days=7)
    userHistory = []
    for history in fullUserHistory:
        date = datetime.strptime(history['date'], '%Y-%m-%d %H:%M:%S')
        if date >= previousWeek and date <= sysdate and (not onlyAccepted or history['status'] == 'accepted'or history['status'] == 'asserted'):
            userHistory.append(history)

    if len(userHistory) == 0:
        return None
    
    return userHistory


def get_user_history_of_month(userId):
    """
    Recupera dalla collection users_food_history del db la cronologia dei suggerimenti alimenatri dell'utente 
    con dato userId dell'ultimo mese.

    Args : 
    - userId : id dell'utente di cui recuperare la cronologia.

    Returns : 
    - userHistory : cronologia dell'ultima settimana dell'utente con dato userId recuperata dal db.
    """
    
    fullUserHistory = userHistoryDB.get_user_history(userId)

    #filter the user history of the month
    sysdate = datetime.today()
    previousMonth = sysdate - timedelta(days=30)
    userHistory = []
    for history in fullUserHistory:
        date = datetime.strptime(history['date'], '%Y-%m-%d %H:%M:%S')
        if date >= previousMonth and date <= sysdate:
            userHistory.append(history)

    if len(userHistory) == 0:
        return None
    
    return userHistory


def clean_temporary_declined_suggestions(userId):
    """
    Rimuove i suggerimenti alimentari temporaneamente rifiutati (con stato "temporary_declined") dalla cronologia dei suggerimenti
    dell'utente con dato userId
    
    Args : 
    - userId : id dell'utente di cui eliminare i suggerimenti temporaneamente rifiutati. 
    """
    userHistoryDB.clean_temporary_declined_suggestions(userId)


def save_user_history(userHistoryJson):
    """
    Salva la data cronologia dei suggerimenti alimentari nel db.
    
    Args:
    - userHistoryJson : suggerimento da salvare nel db.
    """
    userHistoryDB.save_user_history(userHistoryJson)


def build_and_save_user_history(userData, jsonRecipe, status, ingredients_to_remove = None, ingredients_to_add = None):
    """
    Costruisce un oggetto di cronologia suggerimento alimentare istanza della classe UserHistory 
    a partire da una ricetta suggerita, i dati dell'utente, e lo stato di accettazione del suggerimento,
    e lo salva nel db.

    Args:
    - userData : oggetto utente contenente le informazioni dell'utente 
    - jsonRecipe : stringa JSON che rappresenta la ricetta suggerita.
    - status : stato del suggerimento.
    - ingredients_to_remove : evenutali nomi degli ingredienti da rimuovere dalla ricetta prima di salvarla.
    - ingredients_to_add : evenutali nomi degli ingredienti da aggiungere alla ricetta prima di salvarla.
    """

    print("---------------------------------------------------------------------\nJSON RECIPE : \n",jsonRecipe)
    suggestedRecipe = recipe.Recipe.from_json(jsonRecipe)
    suggestedRecipe.display()

    sysdate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    userHistory = uh.UserHistory(userData.id, suggestedRecipe, sysdate, status)
    
    #save the suggestion in the user history
    save_user_history(userHistory.to_plain_json())


def get_consumed_recipes(userId, onlyAccepted = True):

    consumed_recipes = []

    fullUserHistory = userHistoryDB.get_user_history(userId)
        
    #filter the user history of the week
    sysdate = datetime.today()
    previousWeek = sysdate - timedelta(days=7)

    for history in fullUserHistory:
        date = datetime.strptime(history['date'], '%Y-%m-%d %H:%M:%S')
        if date >= previousWeek and date <= sysdate and (not onlyAccepted or history['status'] == 'accepted'or history['status'] == 'asserted'):
            consumed_recipes.append(history['recipe']['name'])

    if len(consumed_recipes) == 0:
        return None

    return consumed_recipes

