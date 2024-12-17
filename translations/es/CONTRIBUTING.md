# Contribuyendo

Este proyecto da la bienvenida a contribuciones y sugerencias. La mayoría de las contribuciones requieren que
aceptes un Acuerdo de Licencia para Contribuyentes (CLA) declarando que tienes el derecho de,
y de hecho, nos otorgas los derechos para usar tu contribución. Para más detalles, visita
<https://cla.microsoft.com>.

> Importante: cuando traduzcas texto en este repositorio, asegúrate de no usar traducción automática. Verificaremos las traducciones a través de la comunidad, así que por favor, solo ofrécete como voluntario para traducciones en idiomas en los que seas competente.

Cuando envíes una solicitud de extracción, un bot de CLA determinará automáticamente si necesitas
proporcionar un CLA y decorará el PR de manera apropiada (por ejemplo, etiqueta, comentario). Simplemente sigue las
instrucciones proporcionadas por el bot. Solo necesitarás hacer esto una vez en todos los repositorios que usen nuestro CLA.

## Código de Conducta

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Para más información, lee las [Preguntas Frecuentes sobre el Código de Conducta](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) o contacta con [opencode@microsoft.com](mailto:opencode@microsoft.com) para cualquier pregunta o comentario adicional.

## ¿Pregunta o Problema?

Por favor, no abras issues en GitHub para preguntas generales de soporte ya que la lista de GitHub debe usarse para solicitudes de características e informes de errores. De esta manera, podemos rastrear más fácilmente problemas o errores reales del código y mantener la discusión general separada del código real.

## Errores tipográficos, Problemas, Errores y contribuciones

Siempre que envíes cambios al repositorio de Generative AI for Beginners, por favor sigue estas recomendaciones.

* Siempre haz un fork del repositorio a tu propia cuenta antes de hacer tus modificaciones
* No combines múltiples cambios en una sola solicitud de extracción. Por ejemplo, envía cualquier corrección de errores y actualizaciones de documentación usando PRs separados
* Si tu solicitud de extracción muestra conflictos de fusión, asegúrate de actualizar tu rama principal local para que sea un espejo de lo que está en el repositorio principal antes de hacer tus modificaciones
* Si estás enviando una traducción, por favor crea un PR para todos los archivos traducidos ya que no aceptamos traducciones parciales del contenido
* Si estás enviando una corrección de error tipográfico o de documentación, puedes combinar modificaciones en un solo PR donde sea adecuado

## Guía General para escribir

- Asegúrate de que todas tus URLs estén entre corchetes cuadrados seguidos de un paréntesis sin espacios adicionales alrededor de ellos o dentro de ellos `[](../..)`.
- Asegúrate de que cualquier enlace relativo (es decir, enlaces a otros archivos y carpetas en el repositorio) comience con un `./` refiriéndose a un archivo o carpeta ubicada en el directorio de trabajo actual o un `../` refiriéndose a un archivo o carpeta ubicada en un directorio de trabajo principal.
- Asegúrate de que cualquier enlace relativo (es decir, enlaces a otros archivos y carpetas en el repositorio) tenga un ID de seguimiento (es decir, `?` o `&` luego `wt.mc_id=` o `WT.mc_id=`) al final de él.
- Asegúrate de que cualquier URL de los siguientes dominios _github.com, microsoft.com, visualstudio.com, aka.ms, y azure.com_ tenga un ID de seguimiento (es decir, `?` o `&` luego `wt.mc_id=` o `WT.mc_id=`) al final de ella.
- Asegúrate de que tus enlaces no tengan un locale específico de país en ellos (es decir, `/en-us/` o `/en/`).
- Asegúrate de que todas las imágenes estén almacenadas en la carpeta `./images`.
- Asegúrate de que las imágenes tengan nombres descriptivos usando caracteres en inglés, números y guiones en el nombre de tu imagen.

## Flujos de Trabajo de GitHub

Cuando envíes una solicitud de extracción, se activarán cuatro flujos de trabajo diferentes para validar las reglas anteriores.
Simplemente sigue las instrucciones listadas aquí para pasar las verificaciones de flujo de trabajo.

- [Verificar Rutas Relativas Rotos](../..)
- [Verificar Rutas Tienen Seguimiento](../..)
- [Verificar URLs Tienen Seguimiento](../..)
- [Verificar URLs No Tienen Locale](../..)

### Verificar Rutas Relativas Rotos

Este flujo de trabajo asegura que cualquier ruta relativa en tus archivos esté funcionando.
Este repositorio se despliega en GitHub pages por lo que debes ser muy cuidadoso cuando escribas los enlaces que unen todo para no dirigir a nadie al lugar equivocado.

Para asegurarte de que tus enlaces estén funcionando correctamente simplemente usa VS code para verificarlo.

Por ejemplo, cuando pases el cursor sobre cualquier enlace en tus archivos se te pedirá que sigas el enlace presionando **ctrl + click**

![Captura de pantalla de VS code seguir enlaces](../../translated_images/vscode-follow-link.png?WT.mc_id=academic-105485-koreyst "Captura de pantalla de VS code indicando seguir un enlace cuando pasas el cursor sobre un enlace.985dc1fa72b20fa525440b38b6babd4013d56bc9a9cbd2e3a10f27244e681ceb.es.")

Si haces clic en un enlace y no funciona localmente, entonces seguramente activará el flujo de trabajo y no funcionará en GitHub.

Para solucionar este problema, intenta escribir el enlace con la ayuda de VS code.

Cuando escribas `./` o `../` VS code te pedirá que elijas entre las opciones disponibles de acuerdo a lo que escribiste.

![Captura de pantalla de VS code seleccionar ruta relativa](../../translated_images/vscode-select-relative-path.png?WT.mc_id=academic-105485-koreyst "Captura de pantalla de VS code indicando seleccionar ruta relativa de una lista emergente.aa7aa416dcb374014324910e36a4e5b42d1fc45bd46a03705e00e438ad2af403.es.")

Sigue la ruta haciendo clic en el archivo o carpeta deseada y estarás seguro de que tu ruta no está rota.

Una vez que agregues la ruta relativa correcta, guarda y envía tus cambios, el flujo de trabajo se activará nuevamente para verificar tus cambios.
Si pasas la verificación, entonces estás listo para continuar.

### Verificar Rutas Tienen Seguimiento

Este flujo de trabajo asegura que cualquier ruta relativa tenga seguimiento en ella.
Este repositorio se despliega en GitHub pages por lo que necesitamos rastrear el movimiento entre los diferentes archivos y carpetas.

Para asegurarte de que tus rutas relativas tengan seguimiento simplemente verifica el siguiente texto `?wt.mc_id=` al final de la ruta.
Si está agregado a tus rutas relativas, entonces pasarás esta verificación.

Si no, podrías recibir el siguiente error.

![Captura de pantalla de comentario de GitHub de rutas faltantes de seguimiento](../../translated_images/github-check-paths-missing-tracking-comment.png?WT.a320886770b936886823dd96e79a9420e314f2e1ea9927a4c9a44c681c741263.es.mc_id=academic-105485-koreyst "captura de pantalla de comentario de github que muestra seguimiento faltante de rutas relativas")

Para solucionar este problema, intenta abrir la ruta del archivo que el flujo de trabajo destacó y agrega el ID de seguimiento al final de las rutas relativas.

Una vez que agregues el ID de seguimiento, guarda y envía tus cambios, el flujo de trabajo se activará nuevamente para verificar tus cambios.
Si pasas la verificación, entonces estás listo para continuar.

### Verificar URLs Tienen Seguimiento

Este flujo de trabajo asegura que cualquier URL web tenga seguimiento en ella.
Este repositorio está disponible para todos, por lo que necesitas asegurarte de rastrear el acceso para saber de dónde viene el tráfico.

Para asegurarte de que tus URLs tengan seguimiento simplemente verifica el siguiente texto `?wt.mc_id=` al final de la URL.
Si está agregado a tus URLs, entonces pasarás esta verificación.

Si no, podrías recibir el siguiente error.

![Captura de pantalla de comentario de GitHub de URLs faltantes de seguimiento](../../translated_images/github-check-urls-missing-tracking-comment.png?WT.77f858835a6ef7e5cc1d6fff996f03e9d28eb482bdf703e6f9617f72a57b8f43.es.mc_id=academic-105485-koreyst "captura de pantalla de comentario de github que muestra seguimiento faltante de urls")

Para solucionar este problema, intenta abrir la ruta del archivo que el flujo de trabajo destacó y agrega el ID de seguimiento al final de las URLs.

Una vez que agregues el ID de seguimiento, guarda y envía tus cambios, el flujo de trabajo se activará nuevamente para verificar tus cambios.
Si pasas la verificación, entonces estás listo para continuar.

### Verificar URLs No Tienen Locale

Este flujo de trabajo asegura que cualquier URL web no tenga un locale específico de país en ella.
Este repositorio está disponible para todos alrededor del mundo, por lo que necesitas asegurarte de no incluir el locale de tu país en las URLs.

Para asegurarte de que tus URLs no tengan un locale de país simplemente verifica el siguiente texto `/en-us/` o `/en/` o cualquier otro locale de idioma en cualquier parte de la URL.
Si no está presente en tus URLs, entonces pasarás esta verificación.

Si no, podrías recibir el siguiente error.

![Captura de pantalla de comentario de GitHub de locale de país agregado](../../translated_images/github-check-country-locale-comment.png?WT.d15ed642ebb74cd1779f9f104cf6030554ca785689515e875c860f78a8cf2601.es.mc_id=academic-105485-koreyst "captura de pantalla de comentario de github que muestra locale de país agregado a urls")

Para solucionar este problema, intenta abrir la ruta del archivo que el flujo de trabajo destacó y elimina el locale de país de las URLs.

Una vez que elimines el locale de país, guarda y envía tus cambios, el flujo de trabajo se activará nuevamente para verificar tus cambios.
Si pasas la verificación, entonces estás listo para continuar.

¡Felicidades! Nos pondremos en contacto contigo lo antes posible con comentarios sobre tu contribución.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción humana profesional. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.