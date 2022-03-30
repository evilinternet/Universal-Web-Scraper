from instagramy import *
username=input("Enter the Username:")
user=InstagramUser(username)

full_name=user.fullname
biography=user.biography
followers=user.number_of_followers
following=user.number_of_followings
posts=user.number_of_posts

data={"Data Type":["Full Name","Biography","Followers","Followings","Posts"],"Scraped Information":[full_name,biography,followers,following,posts]}
df=pd.DataFrame(data,columns=["Data Type","Scraped Information"])

df.to_excel(r' |DESIRED LOCATION| \output.xlsx',index=False,header=True)