import streamlit as st
from PIL import Image
import urllib

x = [int(x) for x in range(31)]
st.title('Practising the streamlit library')


if st.checkbox("Click if  you want to see Cubes of the first 30 numbers"):
    st.markdown("### Given below is the squares of first 30 numbers")
    for i in x:
        st.write("Cube of {} is ".format(i),i**3)
    

st.header("Pick your choice of cars")
car_selection = st.select_slider("Your available choices are :-",['Sports car','Budget car','Luxury car'])
@st.cache(persist = True)
def cars(car_selection):
    if car_selection  == "Sports car":
        urllib.request.urlretrieve("https://www.designnews.com/sites/designnews.com/files/styles/article_featured_retina/public/Design%20News/00-Divo_BUGATTI.jpg", "car_sample1.png")
        img = Image.open("car_sample1.png")
        img = img.resize((700,400))
        return img

    elif car_selection  == "Budget car":
        urllib.request.urlretrieve("https://i2.wp.com/new-politics.net/wp-content/uploads/2019/05/top-budget-cars-in-India.jpg", "car_sample3.png")
        img = Image.open("car_sample3.png")
        img = img.resize((700,400))
        return img

    elif car_selection  == "Luxury car":
        urllib.request.urlretrieve("https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/body-image/public/1-bmw-7-series-730ld-2019-uk-fd-hero-front.jpg", "car_sample2.png")
        img = Image.open("car_sample2.png")
        img = img.resize((700,400))
        return img

car_img = cars(car_selection)
st.image(car_img, caption = " You have selected a {} car".format(car_selection))


st.header("Pick your choice of ice-cream from the sidebar menu")
@st.cache(persist = True)
def ice_cream(ic_selection):
    if ic_selection == "Vanilla":
        urllib.request.urlretrieve("https://5.imimg.com/data5/VE/ML/EN/SELLER-4199470/delicious-vanilla-ice-cream-500x500.jpg", "sample.png")
        img = Image.open("sample.png")
        img = img.resize((700,400))
        return img
        
    elif ic_selection == "Strawberry":
        urllib.request.urlretrieve("https://food.fnr.sndimg.com/content/dam/images/food/fullset/2015/6/19/2/WU1013H_Strawberry-Ice-Cream_s4x3.jpg.rend.hgtvcom.826.620.suffix/1435349504334.jpeg","sample1.png")
        img = Image.open("sample1.png")
        img = img.resize((700,400))
        return img

    elif ic_selection == "Chocolate":
        urllib.request.urlretrieve("https://www.modernhoney.com/wp-content/uploads/2018/08/Homemade-Chocolate-Ice-Cream-1.jpg","sample2.png")
        img = Image.open("sample2.png")
        img = img.resize((700,400))
        return img

    elif ic_selection == "Butterscotch":
        urllib.request.urlretrieve("https://images.herzindagi.info/image/2020/Apr/butterscotch-ice-cream-recipe-two.jpg","sample3.png")
        img = Image.open("sample3.png")
        img = img.resize((700,400))
        return img

ic_selection = st.sidebar.selectbox('Pick your choice of Ice-cream:',['Vanilla','Strawberry','Chocolate','Butterscotch'])
img = ice_cream(ic_selection)
st.image(img , caption = 'You selected {} flavoured ice-cream'.format(ic_selection))