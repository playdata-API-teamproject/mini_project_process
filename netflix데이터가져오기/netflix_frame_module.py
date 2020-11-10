%%writefile C:\myPyCode\팀프로젝트\netflix_frame_module.py
import pandas as pd

df = pd.read_csv("netflix_titles.csv",encoding="latin1")
select = pd.DataFrame(df,columns = ['show_id', 'type', 'title', 'date_added','release_year', 'rating', 'duration','listed_in', 'description'])

def netflix_date_selection(select_col,Name) :
    #select.sort_values(by = ['release_year','date_added']) 날짜별로 구분하기
    selection = select[select[select_col] == Name].sort_values(by = ['release_year','date_added'])
    return selection

def netflix_data_findword(position,Name) :
    find_line = select.loc[select[position].str.contains(Name)].sort_values(by = ['release_year','date_added'])
    return find_line
#     df['email_startswith'] = df['email'].str.startswith(pat='h')     # 좌측값이 입력패턴과 일치 여부
#     df['email_endswith']   = df['email'].str.endswith(pat='com')     # 우측값이 입력패턴과 일치 여부
#     df['email_contains']   = df['email'].str.contains(pat='kr', regex=False) # 값 중 패턴포함 여부
#     df['email_match']      = df['email'].str.match(pat='[a-zA-Z@.]') # 입력패턴과 일치 여부
