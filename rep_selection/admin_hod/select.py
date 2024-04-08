qualities=['leader','captain','incharge','member','lead','administrator']
def responsibilities_check(responsibilities):
    for responsibility in responsibilities:
        for quality in qualities:
            if quality.lower() in responsibility.lower():
                return False
    else:
        return True       
def print_message(data):
        if len(data)>1:
            for datas in data:
                if datas.rep_before is False:
                    print("bye")
                    datas.select=True
                    return
                    
                elif datas.have_responsibilities is False  :
                    print("hello")
                    datas.select=True
                    return 
                elif responsibilities_check(datas.responsibilities):
                    print("hai")
                    datas.select=True
                    return
        else:
            data.select=True
                
