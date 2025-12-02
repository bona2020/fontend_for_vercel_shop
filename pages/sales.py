import streamlit as st
import requests
from pages.products import *

st.header("Sale Page")
st.write("This is where Sales data will go.")

with st.container(border=True):
            st.markdown('#### Sales')
            check = requests.get('https://project-vercel-two.vercel.app/count_sale')
            count_sale = check.json()
            st.markdown(f'##### {count_sale[0]['count']}')
#----------------------------------------------------------------------------------
#1. CREATE A SALE BUTTON:
@st.dialog('CREATE A NEW SALE')
def create_sales_b():
    sal_id =st.number_input('Enter Sale ID',min_value=1)
    sal_date=st.date_input('Enter Sale Date ')
    prod_id=st.number_input('Enter Product ID',min_value=1)
    em_id=st.number_input('Enter Employee ID',min_value=1)
    qty= st.number_input('Enter Quantity',min_value=1)
    tamount=st.number_input('Enter Total Amount',min_value=10)
    sbttn = st.button('Create',type='primary')
    if sbttn :
        create_sale= requests.post(f'https://project-vercel-two.vercel.app/create_sale?sale_id={sal_id}&sale_date={sal_date}&product_id={prod_id}&employee_id={em_id}&quantity={qty}&total_amount={tamount}')
        if create_sale:
            st.toast('😊New Sale Created Sucessfully')
        else:
            st.toast('😓Sale Not Created')
        st.rerun()



#3. UPDATE A SALE BUTTON:
@st.dialog('UPDATE A SALE')
def update_sales_b():
    sal_id =st.number_input('Enter Sale ID',min_value=1)
    sal_date=st.date_input('Enter Sale Date ')
    prod_id=st.number_input('Enter Product ID',min_value=1)
    em_id=st.number_input('Enter Employee ID',min_value=1)
    qty= st.number_input('Enter Quantity',min_value=1)
    tamount=st.number_input('Enter Total Amount',min_value=10)
    sbttn = st.button('Create',type='primary')
    if sbttn :
        update_sale= requests.put(f'https://project-vercel-two.vercel.app/update_sale?sale_id={sal_id}&sale_date={sal_date}&product_id={prod_id}&employee_id={em_id}&quantity={qty}&total_amount={tamount}')
        if update_sale:
            st.toast('😊Sale Updated Sucessfully')
        else:
            st.toast('😓Sale Not Updated')
        st.rerun()

#4. DELETE A SALE BUTTON:
@st.dialog('DELETE A SALE')
def delete_sales_b():
    sal_id =st.number_input('Enter Sale ID',min_value=1)
    sbttn = st.button('Create',type='primary')
    if sbttn :
        delete_sale = requests.delete(f'https://project-vercel-two.vercel.app/delete_sale/{sal_id}')
        if delete_sale:
            st.toast('😊Sale Deleted Sucessfully')
        else:
            st.toast('😓Sale Not Deleted ')
        st.rerun()
#===================================================================================
#Sale Buttons in header side
res = requests.get('https://project-vercel-two.vercel.app')
if res.status_code == 200:
    cls_sbtn=st.columns([1,1,1,1])
    with cls_sbtn[0]:
        create_sbtn= st.button('CREATE SALE',type='primary')
        if create_sbtn:
            create_sales_b()
    with cls_sbtn[1]:
        modify_sbtn = st.button('MODIFY SALE',type='primary')
        if modify_sbtn:
            update_sales_b()
    with cls_sbtn[2]:
        update_sbtn=st.button('UPDATE SALE',type='primary')
        if update_sbtn:
            update_sales_b()
    with cls_sbtn[3]:
        del_sbtn= st.button('DELETE SALE',type='primary')
        if del_sbtn:
            delete_sales_b()
#===============================================================================
    sho_sal = requests.get('https://project-vercel-two.vercel.app/detail_sale/')
    sho_sal =sho_sal.json()
    for sale in sho_sal:
        with st.container(border=True):
            st.markdown(f'ID: [{sale['sale_id']}]'+" | "+ f'📅 Date: {sale['sale_date']}')
            st.markdown(f'##### 🍲[{sale['product_name']}]')
            st.markdown(f'###### 👨‍🍳 Sold By : [{sale['name']}]')
            st.markdown(f'###### Qty: {sale['quantity']}'+ ' X '+f'Unite Price: {product['price']}'+' '+ f' = 💵Total Amount: Rs.{sale['total_amount']}/-')
                