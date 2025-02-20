import streamlit as st
from app.screens.pools_analyses.index import PoolsAnalyses
from app.screens.my_wallet.index import MyWallet

class App:
    def __init__(self):
        self.pages = {}
        self.current_page = None
    
    @staticmethod
    def init() -> st.Page:
        pages = {
            "Resources": [
                st.Page(PoolsAnalyses.page, title="Crew Pools", url_path="/"),
            ],
            "Your account": [
                st.Page(MyWallet.page, title="My Wallet", url_path="my-wallet"),
            ],
            
        }
        pg = st.navigation(pages, position="sidebar", expanded=True)
        pg.run()
        