'''
Created on May 18, 2020

@author: HArihara Ganeshan
'''

def repeat_cols(columns):
    last_non_unnamed = 'Col' if 'unnamed' in columns[0].lower() else columns[0]
    new_columns = []
    new_column = ''
    cnt=1
    for column in columns:
        if 'unnamed' in column.lower():
            if cnt != 0:
                new_column=last_non_unnamed+str(cnt)
                cnt=cnt+1
            else:
                new_column=last_non_unnamed
        else:
            new_column = column
            last_non_unnamed = new_column
            cnt=0
        new_columns.append(new_column)	
    return new_columns

df.columns = repeat_cols(df.columns)

df = df.replace('\n',' ', regex=True)
