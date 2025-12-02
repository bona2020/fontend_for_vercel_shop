import streamlit as st
import requests
from pages.sales import create_sales_b




title = st.title("Welcome to Haridosa Shop")
st.write("Use the sidebar to navigate between pages.")
res = requests.get('https://project-vercel-two.vercel.app')
#=================================================================================
#BUY BUTTON:
@st.dialog('BUY AN ITEM')
def buy(product, employee_id=None):
    sal_id =st.number_input('Enter This Sale ID',min_value=1)
    st.write(sal_id)
    sal_date=st.date_input('Enter Today Date ')
    st.write(sal_date)
    prod_id=st.number_input("Product ID", value=product["product_id"])
    st.write(product['product_name'])
    em_id=st.number_input("Employee ID", min_value=1, value=1)
    qty= st.number_input('How Much Quantity',min_value=1)
    st.write(qty)
    tamount=qty * product["price"]
    st.write(f"Total Amount: Rs.{tamount}/-")
    sbttn = st.button(f'Create',type='primary')
    if sbttn :
        create_sale= requests.post(f'https://project-vercel-two.vercel.app/create_sale?sale_id={sal_id}&sale_date={sal_date}&product_id={prod_id}&employee_id={em_id}&quantity={qty}&total_amount={tamount}')
        if create_sale:
            st.toast('😊New Sale Created Sucessfully')
        else:
            st.toast('😓Sale Not Created')
        st.rerun()
#=========================================================================
if res.status_code == 200:
    stat_cls = st.columns([1,1,1])
#========================================================================
# ANALYTICS: EMPLOYEES     
    with stat_cls[0]:
        with st.container(border=True):
            st.markdown('#### Employees')
            check =requests.get('https://project-vercel-two.vercel.app/count_employee')
            count_em= check.json()
            st.markdown(f'##### {count_em[0]['count']}')
#========================================================================
# ANALYTICS: PRODUCTS     
    with stat_cls[1]:
        with st.container(border=True):
            st.markdown('#### Products')
            check = requests.get('https://project-vercel-two.vercel.app/count_product')
            count_pro = check.json()
            st.markdown(f'##### {count_pro[0]['count']}')
#========================================================================
# ANALYTICS: SALES     
    with stat_cls[2]:
        with st.container(border=True):
            st.markdown('#### Sales')
            check = requests.get('https://project-vercel-two.vercel.app/count_sale')
            count_sale = check.json()
            st.markdown(f'##### {count_sale[0]['count']}')
#========================================================================
    st.divider()
#========================================================================
# TABS
    tabs = st.tabs(['Employees','Products','Sales'])       
#---------------------------------------------------------------------------------------------------------------------
# EMPLOYEES TAB:
    with tabs[0]:
        sho_emp = requests.get('https://project-vercel-two.vercel.app/get_employees')
        sho_emp =sho_emp.json()
        with st.container(border=True):
            for employee in sho_emp:
                with st.container(border=True):
                    this_emp=st.markdown(f'ID: [{employee['employee_id']}]')
                    st.markdown(f'##### 🙋‍♂️Name: {employee['name']}')
                    st.markdown(f'🦺Role: {employee['position']}'+ ' | '+ f'📍Region: {employee['region']}')
#----------------------------------------------------------------------------------------------------------------------
# PRODUCTS TAB:
    with tabs[1]:
        sho_pro = requests.get('https://project-vercel-two.vercel.app/get_products')
        sho_pro =sho_pro.json()
        for product in sho_pro:
            with st.container(border=True):
                this_pro =st.markdown(f'ID: [{product['product_id']}]')
                st.markdown(f'#### 🥣{product['product_name']}')
                st.markdown(f'###### 🥃 Category: {product['category']} | ')  
                this_price= st.markdown(f'##### 💲Price: Rs.{product['price']}/-')
#=====================================================================================================================================================================================================================
                b_buy=st.button(f'BUY',type='primary', key=f"buy_{product['product_id']}")
                if b_buy:
                    buy(product)
#=====================================================================================================================================================================================================================
#----------------------------------------------------------------------------------------------------------------------
# SALES TAB:
    with tabs[2]:
        sho_sal = requests.get('https://project-vercel-two.vercel.app/detail_sale/')
        sho_sal =sho_sal.json()
        for sale in sho_sal:
            with st.container(border=True):
                st.markdown(f'ID: [{sale['sale_id']}]'+" | "+ f'📅 Date: {sale['sale_date']}')
                st.markdown(f'##### 🍲[{sale['product_name']}]')
                st.markdown(f'###### 👨‍🍳 Sold By : [{sale['name']}]')
                st.markdown(f'###### Qty: {sale['quantity']}'+ ' X '+f'Unite Price: {product['price']}'+' '+ f' = 💵Total Amount: Rs.{sale['total_amount']}/-')
                

