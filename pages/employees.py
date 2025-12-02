import streamlit as st
import requests

st.header("Employees Page")
st.write("This is where employee data will go.")

with st.container(border=True):
        st.markdown('#### Employees')
        check =requests.get('https://project-vercel-two.vercel.app/count_employee')
        count_em= check.json()
        st.markdown(f'##### {count_em[0]['count']}')
#=======================================================================================
#1. CREATE EMPLOYEE BUTTON:
@st.dialog('Create An Employee')
def create_new_employee():
    emp_id = st.number_input('Enter Employee ID: ',min_value=1)
    emp_name = st.text_input('Enter Employee Name:')
    emp_position = st.text_input('Enter Employee Position:')
    emp_region = st.selectbox('Select a Region',['Noth','South','East','West','Central'])
    create_btn= st.button('CREATE',type='primary')
    if create_btn :
        create_employee= requests.post(f'https://project-vercel-two.vercel.app/create_employee?employee_id={emp_id}&name={emp_name}&position={emp_position}&region={emp_region}')
        if create_employee:
            st.toast('New Employee Added Successfully')
        else:
            st.toast('Not Created New Employee')
        st.rerun()


#3. MODIFY EMPLOYEE BUTTON:
@st.dialog('Modify Employee')
def modif_employee():
    emp_id =st.number_input('Enter Employee ID',min_value=1)
    emp_name = st.text_input('Enter Employee Name')
    emp_position = st.text_input('Enter Employee Position')
    emp_region = st.selectbox('Select a Region',['North','South','East','West','Central'])
    modif_btn= st.button('Modify',type='primary')
    if modif_btn:
        create_employee= requests.put(f'https://project-vercel-two.vercel.app/update_employee?employee_id={emp_id}&name={emp_name}&position={emp_position}&region={emp_region}')
        if create_employee:
            st.toast('Employee Modified Successfully')
        else:
            st.toast('Employee Not Modified ')
        st.rerun()

#4. DELETE EMPLOYEE BUTTON:
@st.dialog('Delete An Employee')
def dele_employee():
    emp_id = st.number_input('Enter Employee ID',min_value=1)
    dltbtn = st.button('Delete',type='primary')
    if dltbtn:
        delete_emp= requests.delete(f"https://project-vercel-two.vercel.app/delete_employee/{emp_id}")
        if delete_emp:
            st.toast('Employee Deleted')
        else:
            st.toast('Employee Not Deleted')

        st.rerun()
    #------------------------------------------------------------------------
res = requests.get('https://project-vercel-two.vercel.app')
if res.status_code == 200:
    cls_ebtn = st.columns([1,1,1,1])
    with cls_ebtn[0]:
        crete_ebtn= st.button('CREATE  EMPLOYEE',type='primary')
        if crete_ebtn:
            create_new_employee()
    with cls_ebtn[1]:
        modify_ebtn= st.button('MODIFY EMPLOYEE',type='primary')
        if modify_ebtn:
            modif_employee()
    with cls_ebtn[2]:
        updt_ebtn= st.button('UPDATE EMPLOYEE',type='primary')
        if updt_ebtn:
            modif_employee()
    with cls_ebtn[3]:
        del_ebtn= st.button('DELETE EMPLOYEE',type='primary')
        if del_ebtn:
            dele_employee()
#===================================================================================
    sho_emp = requests.get('https://project-vercel-two.vercel.app/get_employees')
    sho_emp =sho_emp.json()
    with st.container(border=True):
        for employee in sho_emp:
            with st.container(border=True):
                st.markdown(f'ID: [{employee['employee_id']}]')
                st.markdown(f'##### Name: {employee['name']}')
                st.markdown(f'Role: {employee['position']}'+ ' | '+ f'Region: {employee['region']}')