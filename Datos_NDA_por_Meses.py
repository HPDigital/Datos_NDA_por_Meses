"""
Datos_NDA_por_Meses
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
import numpy as np 
import seaborn as sns
import sktime as sk


# In[2]:


path1 = "C:\\Users\\HP\\Desktop\\TESIS\\DATOS_NDA_POR_MES_ TESIS\\Carpeta_NDA_Por_mes\\NDA_1_marzo.xlsx"
formato_columnas = {'PedidoId': object,'Cantidad': np.int32,  'PrecioUnitario': np.float64, 'MontoFinal': np.float64,'CodigoProducto': object,  'Producto': object,'Departamento': object,  'Grandes_Categorias': object, 'PedidoId': object,'Id_Cliente': object}
df1=pd.read_excel(path1,dtype=formato_columnas, parse_dates=['Fecha'])
df1['Fecha']= pd.to_datetime(df1['Fecha'])


# In[3]:


path2 = "C:\\Users\\HP\\Desktop\\TESIS\\DATOS_NDA_POR_MES_ TESIS\\Carpeta_NDA_Por_mes\\NDA_2_abril.xlsx"
formato_columnas = {'PedidoId': object,'Cantidad': np.int32,  'PrecioUnitario': np.float64, 'MontoFinal': np.float64,'CodigoProducto': object,  'Producto': object,'Departamento': object,  'Grandes_Categorias': object, 'PedidoId': object,'Id_Cliente': object}
df2=pd.read_excel(path2,dtype=formato_columnas, parse_dates=['Fecha'])
df2['Fecha']= pd.to_datetime(df2['Fecha'])


# In[4]:


path3 = "C:\\Users\\HP\\Desktop\\TESIS\\DATOS_NDA_POR_MES_ TESIS\\Carpeta_NDA_Por_mes\\NDA_3_mayo.xlsx"
formato_columnas = {'PedidoId': object,'Cantidad': np.int32,  'PrecioUnitario': np.float64, 'MontoFinal': np.float64,'CodigoProducto': object,  'Producto': object,'Departamento': object,  'Grandes_Categorias': object, 'PedidoId': object,'Id_Cliente': object}
df3=pd.read_excel(path3,dtype=formato_columnas, parse_dates=['Fecha'])
df3['Fecha']= pd.to_datetime(df3['Fecha'])


# In[5]:


path4 = "C:\\Users\\HP\\Desktop\\TESIS\\DATOS_NDA_POR_MES_ TESIS\\Carpeta_NDA_Por_mes\\NDA_4_junio.xlsx"
formato_columnas = {'PedidoId': object,'Cantidad': np.int32,  'PrecioUnitario': np.float64, 'MontoFinal': np.float64,'CodigoProducto': object,  'Producto': object,'Departamento': object,  'Grandes_Categorias': object, 'PedidoId': object,'Id_Cliente': object}
df4=pd.read_excel(path4,dtype=formato_columnas, parse_dates=['Fecha'])
df4['Fecha']= pd.to_datetime(df4['Fecha'])


# In[6]:


path5 = "C:\\Users\\HP\\Desktop\\TESIS\\DATOS_NDA_POR_MES_ TESIS\\Carpeta_NDA_Por_mes\\NDA_5_julio.xlsx"
formato_columnas = {'PedidoId': object,'Cantidad': np.int32,  'PrecioUnitario': np.float64, 'MontoFinal': np.float64,'CodigoProducto': object,  'Producto': object,'Departamento': object,  'Grandes_Categorias': object, 'PedidoId': object,'Id_Cliente': object}
df5=pd.read_excel(path5,dtype=formato_columnas, parse_dates=['Fecha'])
df5['Fecha']= pd.to_datetime(df5['Fecha'])


# In[7]:


path6 = "C:\\Users\\HP\\Desktop\\TESIS\\DATOS_NDA_POR_MES_ TESIS\\Carpeta_NDA_Por_mes\\NDA_6_agosto.xlsx"
formato_columnas = {'PedidoId': object,'Cantidad': np.int32,  'PrecioUnitario': np.float64, 'MontoFinal': np.float64,'CodigoProducto': object,  'Producto': object,'Departamento': object,  'Grandes_Categorias': object, 'PedidoId': object,'Id_Cliente': object}
df6=pd.read_excel(path6,dtype=formato_columnas, parse_dates=['Fecha'])
df6['Fecha']= pd.to_datetime(df6['Fecha'])


# In[8]:


path7 = "C:\\Users\\HP\\Desktop\\TESIS\\DATOS_NDA_POR_MES_ TESIS\\Carpeta_NDA_Por_mes\\NDA_7_septiembre.xlsx"
formato_columnas = {'PedidoId': object,'Cantidad': np.int32,  'PrecioUnitario': np.float64, 'MontoFinal': np.float64,'CodigoProducto': object,  'Producto': object,'Departamento': object,  'Grandes_Categorias': object, 'PedidoId': object,'Id_Cliente': object}
df7=pd.read_excel(path7,dtype=formato_columnas, parse_dates=['Fecha'])
df7['Fecha']= pd.to_datetime(df7['Fecha'])


# In[9]:


path8 = "C:\\Users\\HP\\Desktop\\TESIS\\DATOS_NDA_POR_MES_ TESIS\\Carpeta_NDA_Por_mes\\NDA_8_octubre.xlsx"
formato_columnas = {'PedidoId': object,'Cantidad': np.int32,  'PrecioUnitario': np.float64, 'MontoFinal': np.float64,'CodigoProducto': object,  'Producto': object,'Departamento': object,  'Grandes_Categorias': object, 'PedidoId': object,'Id_Cliente': object}
df8=pd.read_excel(path8,dtype=formato_columnas, parse_dates=['Fecha'])
df8['Fecha']= pd.to_datetime(df8['Fecha'])


# In[10]:


path9 = "C:\\Users\\HP\\Desktop\\TESIS\\DATOS_NDA_POR_MES_ TESIS\\Carpeta_NDA_Por_mes\\NDA_9_noviembre.xlsx"
formato_columnas = {'PedidoId': object,'Cantidad': np.int32,  'PrecioUnitario': np.float64, 'MontoFinal': np.float64,'CodigoProducto': object,  'Producto': object,'Departamento': object,  'Grandes_Categorias': object, 'PedidoId': object,'Id_Cliente': object}
df9=pd.read_excel(path9,dtype=formato_columnas, parse_dates=['Fecha'])
df9['Fecha']= pd.to_datetime(df9['Fecha'])


# In[11]:


frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9]
df=pd.concat(frames, axis=0, ignore_index=True)


# In[12]:


df.dtypes


# In[13]:


df.describe()


# In[14]:


df.head()


# In[15]:


dfpronostico=df[['Fecha','MontoFinal']]


# In[16]:


#dfpronostico=dfpronostico.set_index('Fecha')


# In[17]:


#dfpronostico=dfpronostico.resample('d').mean()


# In[18]:


dfpronostico


# In[19]:


#sns.relplot(data=dfpronostico, kind="line", height=5, aspect=3)


# In[20]:


dfpronostico= dfpronostico.rename(columns={'Fecha':'ds', 'MontoFinal':'y'})


# In[21]:


dfpronostico


# In[22]:


import fbprophet


# In[23]:


df_prophet=fbprophet.Prophet(changepoint_prior_scale=0.15)


# In[24]:


df_prophet.fit(dfpronostico)


# In[25]:


df2_pronostico=df_prophet.make_future_dataframe(periods=30*1 , freq="D")


# In[26]:


df2_pronostico=df_prophet.predict(df2_pronostico)


# In[27]:


df_prophet.plot(df2_pronostico, xlabel = 'Fecha', ylabel= 'MontoFinal')


# In[28]:


sns.relplot(data=df2_pronostico, kind="line", height=5, aspect=3)


# In[29]:


df2_pronostico


# In[30]:


df2_pronostico_final = df2_pronostico[['ds','trend']]


# In[31]:


dfpronostico=dfpronostico.set_index('ds')
df2_pronostico_final=df2_pronostico_final.set_index('ds')


# In[32]:


dfpronostico=dfpronostico.resample('d').mean()
df2_pronostico_final=df2_pronostico_final.resample('d').mean()


# In[33]:


mergedDf = dfpronostico.merge(df2_pronostico_final, how='outer', left_index=True, right_index=True)


# In[34]:


sns.relplot(data=mergedDf, kind="line", height=5, aspect=3)


# In[35]:


mergedDf


# In[ ]:




