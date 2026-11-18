# Contribuyendo

Este proyecto recibe contribuciones y sugerencias con gusto. La mayoría de las contribuciones requieren que usted
acepte un Acuerdo de Licencia de Contribuidor (CLA) declarando que tiene el derecho de,
y de hecho otorga, los derechos para que usemos su contribución. Para más detalles, visite
<https://cla.microsoft.com>.

> Importante: al traducir texto en este repositorio, por favor asegúrese de no usar traducción automática. Verificaremos las traducciones a través de la comunidad, así que por favor ofrézcase solo para traducir en idiomas que domine bien.

Cuando envíe una solicitud de extracción, un CLA-bot determinará automáticamente si necesita
proporcionar un CLA y adornará el PR adecuadamente (por ejemplo, etiqueta, comentario). Simplemente siga las
instrucciones proporcionadas por el bot. Solo necesitará hacer esto una vez en todos los repositorios que usan nuestro CLA.

## Código de Conducta

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Para más información lea las [Preguntas Frecuentes sobre el Código de Conducta](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) o contacte a [opencode@microsoft.com](mailto:opencode@microsoft.com) con cualquier pregunta o comentario adicional.

## ¿Pregunta o Problema?

Por favor, no abra incidencias en GitHub para preguntas generales de soporte, ya que la lista de GitHub debe usarse para solicitudes de características e informes de errores. De esta manera podemos rastrear más fácilmente los problemas o errores reales del código y mantener la discusión general separada del código en sí.

## Errores tipográficos, problemas, fallos y contribuciones

Siempre que envíe cambios al repositorio Generative AI for Beginners, por favor siga estas recomendaciones.

* Siempre bifurque el repositorio a su propia cuenta antes de hacer sus modificaciones
* No combine múltiples cambios en una sola solicitud de extracción. Por ejemplo, envíe cualquier corrección de errores y actualizaciones de documentación usando PRs separados
* Si su solicitud de extracción muestra conflictos de fusión, asegúrese de actualizar su main local para reflejar exactamente lo que está en el repositorio main antes de hacer sus modificaciones
* Si está enviando una traducción, por favor cree una sola PR para todos los archivos traducidos, ya que no aceptamos traducciones parciales del contenido
* Si está enviando una corrección tipográfica o de documentación, puede combinar modificaciones en una única PR cuando sea apropiado

## Alcance editorial y productos de terceros

Este currículo se centra en tecnologías Microsoft y estándares abiertos neutrales respecto a proveedores. Las contribuciones deben tener un propósito educativo claro y no deben estar destinadas principalmente a introducir o promover un producto comercial de terceros, servicio alojado, modelo, enrutador, SDK, servidor MCP u otra oferta específica de un proveedor.

El software de código abierto y las dependencias de terceros pueden ser referenciados cuando sean necesarios para explicar un estándar abierto o un escenario de interoperabilidad, se presenten de forma neutral y no estén centrados en un producto o punto de enlace alojado de un proveedor. Si su contribución propuesta incluye un producto o servicio específico de un proveedor, abra una incidencia y obtenga aprobación del mantenedor antes de enviar una solicitud de extracción.

Los contribuyentes deben divulgar cualquier relación laboral, propiedad, patrocinio u otra afiliación relevante con un producto o servicio mencionado en su contribución. No incluya reclamaciones sin soporte sobre precios, rendimiento, seguridad, privacidad o comparativas. Los ejemplos ejecutables no deben transmitir datos del alumno ni realizar acciones públicas a través de un servicio externo de terceros por defecto.

## Guía general para escribir

- Asegúrese de que todos sus URLs estén entre corchetes seguidos por paréntesis sin espacios adicionales alrededor o dentro de ellos `[]()`.
- Asegúrese de que cualquier enlace relativo (es decir, enlaces a otros archivos y carpetas en el repositorio) comience con un `./` que se refiere a un archivo o carpeta ubicada en el directorio de trabajo actual o un `../` que se refiere a un archivo o carpeta ubicada en un directorio de trabajo padre.
- Asegúrese de que cualquier enlace relativo (es decir, enlaces a otros archivos y carpetas en el repositorio) tenga un ID de seguimiento (es decir, `?` o `&` luego `wt.mc_id=` o `WT.mc_id=`) al final.
- Asegúrese de que cualquier URL de los siguientes dominios _github.com, microsoft.com, visualstudio.com, aka.ms y azure.com_ tenga un ID de seguimiento (es decir, `?` o `&` luego `wt.mc_id=` o `WT.mc_id=`) al final.
- Asegúrese de que sus enlaces no tengan localidad específica de país en ellos (es decir, `/en-us/` o `/en/`).
- Asegúrese de que todas las imágenes estén almacenadas en la carpeta `./images`.
- Asegúrese de que las imágenes tengan nombres descriptivos usando caracteres en inglés, números y guiones en el nombre de su imagen.

## Flujos de trabajo de GitHub

Cuando envíe una solicitud de extracción, se activarán cuatro flujos de trabajo diferentes para validar las reglas anteriores.
Simplemente siga las instrucciones listadas aquí para pasar las verificaciones del flujo de trabajo.

- [Verificar rutas relativas rotas](#check-broken-relative-paths)
- [Verificar que las rutas tengan seguimiento](#check-paths-have-tracking)
- [Verificar que las URLs tengan seguimiento](#check-urls-have-tracking)
- [Verificar que las URLs no tengan localidad](#check-urls-dont-have-locale)

### Verificar rutas relativas rotas

Este flujo de trabajo asegura que cualquier ruta relativa en sus archivos funcione.
Este repositorio está desplegado en GitHub Pages, por lo que debe tener mucho cuidado al escribir los enlaces que enlazan todo para no dirigir a nadie al lugar equivocado.

Para asegurarse de que sus enlaces funcionan correctamente simplemente use VS Code para verificar eso.

Por ejemplo, cuando pase el cursor sobre cualquier enlace en sus archivos se le mostrará la opción de seguir el enlace presionando **ctrl + click**

![Captura de pantalla de VS Code siguiendo enlaces](../../translated_images/es/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Captura de pantalla del aviso de VS Code para seguir un enlace cuando pasa el cursor sobre un enlace.")

Si hace clic en un enlace y no funciona localmente, seguramente activará el flujo de trabajo y no funcionará en GitHub.

Para solucionar este problema, intente escribir el enlace con la ayuda de VS Code.

Cuando escriba `./` o `../`, VS Code le sugerirá opciones disponibles según lo que escribió.

![Captura de pantalla de VS Code seleccionando ruta relativa](../../translated_images/es/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Captura de pantalla del aviso de VS Code para seleccionar ruta relativa desde una lista desplegable.")

Siga la ruta haciendo clic en el archivo o carpeta deseada y así tendrá la seguridad de que su ruta no está rota.

Una vez agregue la ruta relativa correcta, guarde y haga push de sus cambios, el flujo de trabajo se activará nuevamente para verificar sus cambios.
Si pasa la verificación, entonces está listo para continuar.

### Verificar que las rutas tengan seguimiento

Este flujo de trabajo asegura que cualquier ruta relativa tenga un seguimiento incluido.
Este repositorio está desplegado en GitHub Pages, por lo que necesitamos rastrear el movimiento entre los diferentes archivos y carpetas.

Para asegurarse de que sus rutas relativas tengan seguimiento, simplemente verifique que el texto `?wt.mc_id=` esté al final de la ruta.
Si está añadido a sus rutas relativas, pasará esta verificación.

Si no, puede recibir el siguiente error.

![Captura de pantalla de comentario de GitHub verificando rutas sin seguimiento](../../translated_images/es/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Captura de pantalla de comentario de GitHub que muestra rutas relativas sin seguimiento")

Para solucionar este problema, intente abrir la ruta del archivo que resaltó el flujo de trabajo y agregue el ID de seguimiento al final de las rutas relativas.

Una vez agregado el ID de seguimiento, guarde y haga push de sus cambios, el flujo de trabajo se activará nuevamente para verificar sus cambios.
Si pasa la verificación, entonces está listo para continuar.

### Verificar que las URLs tengan seguimiento

Este flujo de trabajo asegura que cualquier URL web tenga un seguimiento incluido.
Este repositorio está disponible para todos, por lo que debe asegurarse de rastrear el acceso para saber de dónde viene el tráfico.

Para asegurarse de que sus URLs tengan seguimiento, simplemente verifique que el texto `?wt.mc_id=` esté al final de la URL.
Si está añadido a sus URLs, pasará esta verificación.

Si no, puede recibir el siguiente error.

![Captura de pantalla de comentario de GitHub verificando URLs sin seguimiento](../../translated_images/es/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Captura de pantalla de comentario de GitHub que muestra URLs sin seguimiento")

Para solucionar este problema, intente abrir la ruta del archivo que resaltó el flujo de trabajo y agregue el ID de seguimiento al final de las URLs.

Una vez agregado el ID de seguimiento, guarde y haga push de sus cambios, el flujo de trabajo se activará nuevamente para verificar sus cambios.
Si pasa la verificación, entonces está listo para continuar.

### Verificar que las URLs no tengan localidad

Este flujo de trabajo asegura que cualquier URL web no tenga una localidad específica de país en ella.
Este repositorio está disponible para todo el mundo, por lo que debe asegurarse de no incluir la localidad de su país en las URLs.

Para asegurarse de que sus URLs no tengan la localidad del país, simplemente verifique que no esté presente el texto `/en-us/` o `/en/` o cualquier otra localidad de idioma en la URL.
Si no está presente en sus URLs, pasará esta verificación.

Si está presente, puede recibir el siguiente error.

![Captura de pantalla de comentario de GitHub verificando localidad de país en URLs](../../translated_images/es/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Captura de pantalla de comentario de GitHub que muestra localidad de país añadida a URLs")

Para solucionar este problema, intente abrir la ruta del archivo que resaltó el flujo de trabajo y elimine la localidad del país de las URLs.

Una vez eliminada la localidad del país, guarde y haga push de sus cambios, el flujo de trabajo se activará nuevamente para verificar sus cambios.
Si pasa la verificación, entonces está listo para continuar.

¡Felicidades! Nos pondremos en contacto con usted lo antes posible con comentarios sobre su contribución.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->