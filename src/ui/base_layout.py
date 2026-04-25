import streamlit as st
def background_home():
    st.markdown("""
   <style> 
                 .stApp{
                background:#5865F2 !important;
            
                
                }

             .stApp div[data-testid="stcolumn"]{
                background-color:#E0E3FF !important;
                padding:2.5rem !important;
                border-radius:5rem !important;}

     </style>  """

 ,unsafe_allow_html=True)
    


def background_dashboard():
    st.markdown("""
   <style>  .stApp{
                background:#E0E3FF !important;
            ;
                
                }
""" ,unsafe_allow_html=True)



def base_layout():
    st.markdown("""
   <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
            
                


             /*hide top bar and footer*/
                #Mainmenu,footer,header{
                    visibility:hidden;
                }
                .block-cointainer{
                padding-top:1.5rem !important;}

                h1{
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size:3.5rem !important;
                    line-height:1.2 !important;
                    margin-bottom:orem !important;
                }
                
                
                 h2{
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size:2rem !important;
                    line-height:1.2 !important;
                    margin-bottom:orem !important;
                    
                }

                h3,h4,p{
                   font-family:'outfit',san-serif ;
                }

                 button[kind="primary"]{
                    border-radius:1.5rem !important;
                    color:#848EE6 !important;
                    background-color:#E9EBF3 !important;
                    # padding: 10px 20px !important;
                    border :none !important;
                    transition:transform .2s ease-in-out !important;
                
                }


                button[kind="secondary"]{
                    border-radius:1.5rem !important;
                    color:EB459E !important;
                    background-color:#EB459E !important;
                    padding: 10px 20px !important;
                    border :none !important;
                    transition:transform .2s ease-in-out !important;}
                

                button[kind="tertiary"]{
                    border-radius:1.5rem !important;
                    color:black !important;
                    background-color:#EB459E !important;
                    padding: 10px 20px !important;
                    border :none !important;
                    transition:transform .25s ease-in-out !important;}
                

                button:hover{
                   transform:scale(1.05) !important;
                }






                }

        </style>
                
                
""" ,unsafe_allow_html=True)


     
    