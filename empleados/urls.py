from django.urls import path
from . import views
from .views import buscar_productos, search_history_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    # urls de productos
    path('', views.inicio, name='inicio'),
    path('registrar-nuevo-empleado/', views.registrar_empleado,
         name='registrar_empleado'),
    path('lista-de-empleados/', views.listar_empleados, name='listar_empleados'),

    path('detalles-del-empleado/<str:id>/',views.detalles_empleado, name='detalles_empleado'),

    path('formulario-para-actualizar-empleado/<str:id>/',
         views.view_form_update_empleado, name='view_form_update_empleado'),

    

    path('actualizar-empleado/<str:id>/',
         views.actualizar_empleado, name='actualizar_empleado'),
    path('eliminar-empleado/', views.eliminar_empleado, name='eliminar_empleado'),


    path('descargar-informe-empleados',
         views.informe_empleado, name="informe_empleado"),
    path('subir-data-xlsx/', views.cargar_archivo, name='subir_data_xlsx'),
    path('formulario-para-la-carga-masiva-de-empleados/', views.view_form_carga_masiva, name='view_form_carga_masiva'),
    
    
     #url del carrito
     path('agregar-producto/<int:empleado_id>/', views.agregar_producto, name='agregar_producto'),
     path('limpiar/', views.limpiar_carrito, name="CLS"),
     path('carrito/', views.carrito_view, name='carrito_view'),
     path('carrito/sumar/<str:key>/', views.sumar_producto_ajax, name='SUMAR'),
     path('carrito/restar/<str:key>/', views.restar_producto_ajax, name='RESTAR'),
     path('carrito/eliminar/<str:key>/', views.eliminar_producto_ajax, name='ELIMINAR'),


    
    
    #url del login y logout
     path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'), 
     path('password_reset/', auth_views.PasswordResetView.as_view(template_name='empleado/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='empleado/password_reset_done.html'), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='empleado/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='empleado/password_reset_complete.html'), name='password_reset_complete'),



    # Historial de búsqueda+ barra de búsqueda
    path('buscar/', views.buscar_productos, name='buscar_productos'),
     path('search_history_view/',views.search_history_view, name='search_history'),
     path('historial/eliminar/<int:pk>/', views.eliminar_busqueda, name='eliminar_busqueda'),
     path('historial/eliminar-todo/', views.eliminar_todo_historial, name='eliminar_todo_historial'),

     #para enviar pedido
     path('pago-movil/', views.pago_movil, name='pago_movil'),
     path('efectivo/', views.efectivo, name='efectivo'),
     path('confirmar-reemplazo/<int:producto_id>/',views.confirmar_reemplazo, name='confirmar_reemplazo'),
     path('reemplazar-producto/<int:producto_id>/', views.reemplazar_producto, name='reemplazar_producto'),
     path('efectivo.html', views.vista_efectivo, name='efectivo'),
     

     #generar pdf
     path('generar-pdf-pedido/', views.generar_pdf_pedido, name='generar_pdf_pedido'),
     path('generar-pdf-efectivo/', views.generar_pdf_efectivo, name='generar_pdf_efectivo'),

     #historial de compras
     path('historial/', views.historial_compras, name='historial_compras'),

     #cuenta de usuario
     path('cuenta/', views.cuenta_view, name='cuenta'),

     #resumen de ventas
    path('historial-general/', views.historial_general_compras, name='historial_general_compras'),

    path('resumen/exportar/', views.exportar_excel, name='exportar_excel'),
    path('pedidos/<int:pk>/', views.pedido_detalle, name='pedido_detalle'),
     path('resumen-mensual/', views.resumen_mensual_ventas, name='resumen_mensual_ventas'),
     path('ranking/', views.ranking_usuarios, name='ranking_usuarios'),
    path('compras/<int:usuario_id>/', views.compras_por_usuario, name='compras_por_usuario'),
     path('ranking-productos/', views.ranking_productos, name='ranking_productos'),

     #informacion de la tienda
     path('info-tienda/', views.info_tienda_view, name='info_tienda'),

     #stok de productos por acabarse 
     path('productos-alerta/', views.productos_alerta_view, name='productos_alerta'),
         
     #ayuda
     path('ayuda/', views.como_comprar, name='como_comprar'),

     #papelera de productos
     path('papelera/', views.papelera_productos, name='papelera_productos'),
     path('restaurar-empleado/', views.restaurar_empleado, name='restaurar_empleado'),

     #anular pedido
     path('anular-pedido/', views.anular_pedido, name='anular_pedido'),





]

   


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)