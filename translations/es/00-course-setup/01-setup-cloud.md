<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T13:34:15+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "es"
}
-->
# Configuración en la nube ☁️ – GitHub Codespaces

**Usa esta guía si no quieres instalar nada en tu equipo.**  
Codespaces te ofrece una instancia gratuita de VS Code en el navegador con todas las dependencias ya instaladas.

---

## 1.  ¿Por qué Codespaces?

| Beneficio | Qué significa para ti |
|-----------|----------------------|
| ✅ Sin instalaciones | Funciona en Chromebook, iPad, PCs de laboratorio escolar… |
| ✅ Contenedor de desarrollo preconfigurado | Python 3, Node.js, .NET, Java ya incluidos |
| ✅ Cuota gratuita | Las cuentas personales reciben **120 horas-núcleo / 60 GB-horas al mes** |

> 💡 **Tip**  
> Mantén tu cuota disponible **deteniendo** o **eliminando** los codespaces que no uses  
> (Ver ▸ Paleta de comandos ▸ *Codespaces: Stop Codespace*).

---

## 2.  Crea un Codespace (con un solo clic)

1. **Haz un fork** de este repositorio (botón **Fork** arriba a la derecha).  
2. En tu fork, haz clic en **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Diálogo mostrando los botones para crear un codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Se abrirá una ventana de VS Code en el navegador y el contenedor de desarrollo comenzará a construirse.
Esto tarda **~2 minutos** la primera vez.

## 3. Agrega tu clave API (de forma segura)

### Opción A Secrets de Codespaces — Recomendado

1. ⚙️ Icono de engranaje -> Paleta de comandos -> Codespaces : Manage user secret -> Add a new secret.
2. Nombre: OPENAI_API_KEY
3. Valor: pega tu clave → Add secret

Listo—nuestro código la detectará automáticamente.

### Opción B Archivo .env (si realmente lo necesitas)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.