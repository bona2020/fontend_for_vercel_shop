import streamlit as st
import requests
st.header("Products Page")
st.write("This is where Products data will go.")

with st.container(border=True):
    st.markdown('#### Products')
    check = requests.get('https://project-vercel-two.vercel.app/count_product')
    count_pro = check.json()
    st.markdown(f'##### {count_pro[0]['count']}')
#------------------------------------------------------------------------
#1. CREATE PRODUCT BUTTON:
@st.dialog('CREATE NEW PRODUCT')
def create_product_s():
    pro_id = st.number_input('Enter Product ID',min_value=1)
    pro_name = st.text_input('Enter Product Name')
    pro_cat = st.selectbox('Select Category',['Fast Food','Healthy','Drinks','Side','Dessert'])
    pro_price=st.number_input('Enter Product Price',min_value=1)
    cpbtn = st.button('Create',type='primary')
    if cpbtn:
        create_pro = requests.post(f'https://project-vercel-two.vercel.app/create_product?product_id={pro_id}&product_name={pro_name}&category={pro_cat}&price={pro_price}')
        if create_pro:
            st.toast('New Product Create Successfully')
        else:
            st.toast('not Created')

        st.rerun()

#2. MODIFY PRODUCT BUTTON:
@st.dialog('MODIFY PRODUCT')
def update_product_s():
    pro_id =st.number_input('Enter Product ID',min_value=1)
    pro_name=st.text_input('Enter Product Name')
    pro_cat= st.selectbox('Select Category',['Fast Food','Healthy','Drinks','Side','Dessert'])
    pro_price=st.number_input('Enter Product Price',min_value=1)
    mpbtn = st.button('Modify',type='primary')
    if mpbtn:
        update_pro = requests.put(f'https://project-vercel-two.vercel.app/update_product?product_id={pro_id}&product_name={pro_name}&category={pro_cat}&price={pro_price}')
        if update_pro:
            st.toast('Product Modified Successfully')
        else:
            st.toast('Product Not Modified')
        st.rerun()



#4. DELETE PRODUCT BUTTON:
@st.dialog('DELETE PRODUCT')
def delete_product_s():
    pro_id = st.number_input('Enter Product ID',min_value=1)
    dpbtn =st.button('Delete',type='primary')
    if dpbtn:
        delete_pro = requests.delete(f'https://project-vercel-two.vercel.app/delete_product/{pro_id}')
        if delete_pro:
            st.toast('Product Deleted Successfully')
        else:
            st.toast('Product Not Deleted / Not Found')
        st.rerun()
#----------------------------------------------------------------------------------
res = requests.get('https://project-vercel-two.vercel.app')
if res.status_code == 200:
    cls_pbtn = st.columns([1,1,1,1])
    with cls_pbtn[0]:
        create_pbtn = st.button('CREATE PRODUCT',type='primary')
        if create_pbtn:
            create_product_s()

    with cls_pbtn[1]:
        modify_pbtn=st.button('MODIFY PRODUCT',type='primary')
        if modify_pbtn:
            update_product_s()
    with cls_pbtn[2]:
        update_pbtn = st.button('UPDATE PRODUCT',type='primary')
        if update_pbtn:
            update_product_s()
    with cls_pbtn[3]:
        del_pbtn=st.button('DELETE PRODUCT',type='primary')
        if del_pbtn:
            delete_product_s()
 #================================================================================
    sho_pro = requests.get('https://project-vercel-two.vercel.app/get_products')
    sho_pro =sho_pro.json()
    for product in sho_pro:
        with st.container(border=True):
            st.markdown(f'ID: [{product['product_id']}]')
            st.markdown(f'#### {product['product_name']}')
            st.markdown(f'###### Category: {product['category']}'+ ' | '+ f'Price: Rs.{product['price']}/-')