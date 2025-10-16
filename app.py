import streamlit as st
from pymongo import MongoClient

client = MongoClient('mongodb://mongodb:27017/')
db = client['eshop']
collection = db['clientes']

st.title("E-Shop Brasil - Gestão de Clientes")

menu = st.sidebar.selectbox("Menu", ["Inserir", "Consultar", "Editar", "Excluir", "Concatenar"])

if menu == "Inserir":
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    if st.button("Salvar"):
        collection.insert_one({"nome": nome, "email": email})
        st.success("Cliente inserido com sucesso!")

elif menu == "Consultar":
    clientes = list(collection.find())
    st.write(clientes)

elif menu == "Editar":
    id_cliente = st.text_input("ID do cliente a editar")
    novo_nome = st.text_input("Novo nome")
    novo_email = st.text_input("Novo email")
    if st.button("Atualizar"):
        from bson.objectid import ObjectId
        collection.update_one({"_id": ObjectId(id_cliente)}, {"$set": {"nome": novo_nome, "email": novo_email}})
        st.success("Cliente atualizado!")

elif menu == "Excluir":
    id_cliente = st.text_input("ID do cliente a excluir")
    if st.button("Excluir"):
        from bson.objectid import ObjectId
        collection.delete_one({"_id": ObjectId(id_cliente)})
        st.success("Cliente excluído!")

elif menu == "Concatenar":
    clientes = list(collection.find())
    for cliente in clientes:
        nome_email = f"{cliente.get('nome', '')} <{cliente.get('email', '')}>"
        st.write(nome_email)
