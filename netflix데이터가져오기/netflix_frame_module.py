import pandas as pd

df = pd.read_csv("netflix_titles.csv",encoding="latin1")
select = pd.DataFrame(df,columns = ['show_id', 'type', 'title', 'date_added','release_year', 'rating', 'duration','listed_in', 'description'])

def netflix_date_selection(select_col,Name) :
    #select.sort_values(by = ['release_year','date_added']) 날짜별로 구분하기
    selection = select[select[select_col] == Name].sort_values(by = ['release_year','date_added'])
    return selection
    
