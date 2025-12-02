import streamlit as st
import requests




title = st.title("Welcome to Haridosa Shop")
st.write("Use the sidebar to navigate between pages.")
res = requests.get('https://project-vercel-two.vercel.app')
if res.status_code == 200:
    stat_cls = st.columns([1,1,1])
    with stat_cls[0]:
        with st.container(border=True):
            st.markdown('#### Employees')
            check =requests.get('https://project-vercel-two.vercel.app/count_employee')
            count_em= check.json()
            st.markdown(f'##### {count_em[0]['count']}')
    with stat_cls[1]:
        with st.container(border=True):
            st.markdown('#### Products')
            check = requests.get('https://project-vercel-two.vercel.app/count_product')
            count_pro = check.json()
            st.markdown(f'##### {count_pro[0]['count']}')
    with stat_cls[2]:
        with st.container(border=True):
            st.markdown('#### Sales')
            check = requests.get('https://project-vercel-two.vercel.app/count_sale')
            count_sale = check.json()
            st.markdown(f'##### {count_sale[0]['count']}')
    st.divider()
    tabs = st.tabs(['Employees','Products','Sales'])       
    with tabs[0]:
        sho_emp = requests.get('https://project-vercel-two.vercel.app/get_employees')
        sho_emp =sho_emp.json()
        with st.container(border=True):
            for employee in sho_emp:
                with st.container(border=True):
                    st.markdown(f'ID: [{employee['employee_id']}]')
                    st.markdown(f'##### Name: {employee['name']}')
                    st.markdown(f'Role: {employee['position']}'+ ' | '+ f'Region: {employee['region']}')
    with tabs[1]:
        sho_pro = requests.get('https://project-vercel-two.vercel.app/get_products')
        sho_pro =sho_pro.json()
        for product in sho_pro:
            with st.container(border=True):
                st.markdown(f'ID: [{product['product_id']}]')
                st.markdown(f'#### {product['product_name']}')
                st.markdown(f'###### Category: {product['category']}'+ ' | '+ f'Price: Rs.{product['price']}/-')
    with tabs[2]:
        sho_sal = requests.get('https://project-vercel-two.vercel.app/get_sales')
        sho_sal =sho_sal.json()
        for sale in sho_sal:
            with st.container(border=True):
                st.markdown(f'ID: [{sale['sale_id']}]'+" | "+ f'Date: {sale['sale_date']}')
                st.markdown(f'##### Product N#: [{sale['product_id']}]')
                st.markdown(f'###### Sold By Employee N#: [{sale['employee_id']}]')
                st.markdown(f'###### Qty: {sale['quantity']}'+ ' | '+ f'Total Amount: Rs.{sale['total_amount']}/-')
                

