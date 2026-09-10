# Configuración en la nube ☁️ – GitHub Codespaces

**Utiliza esta guía si no quieres instalar nada localmente.**  
Codespaces te brinda una instancia gratuita de VS Code en el navegador con todas las dependencias preinstaladas.

---

## 1.  ¿Por qué Codespaces?

| Beneficio | Qué significa para ti |
|---------|----------------------|
| ✅ Sin instalaciones | Funciona en Chromebook, iPad, PC de laboratorios escolares… |
| ✅ Contenedor de desarrollo preconstruido | Python 3, Node.js, .NET, Java ya dentro |
| ✅ Cuota gratuita | Las cuentas personales obtienen **120 horas núcleo / 60 GB-horas por mes** |

> 💡 **Consejo**  
> Mantén tu cuota saludable **deteniendo** o **eliminando** codespaces inactivos  
> (Ver ▸ Paleta de comandos ▸ *Codespaces: Detener Codespace*).

---

## 2.  Crear un Codespace (con un clic)

1. **Haz un fork** de este repositorio (botón **Fork** en la esquina superior derecha).  
2. En tu fork, haz clic en **Code ▸ Codespaces ▸ Crear codespace en main**.  
   ![Diálogo mostrando botones para crear un codespace](../../../translated_images/es/who-will-pay.4c0609b1c7780f44.webp)

✅ Se abre una ventana de VS Code en el navegador y el contenedor de desarrollo comienza a construirse.
Esto toma **~2 minutos** la primera vez.

## 3. Agrega tu clave API (la forma segura)

### Opción A Secrets de Codespaces — Recomendado

1. ⚙️ Icono de engranaje -> Paleta de comandos -> Codespaces : Administrar secreto de usuario -> Agregar un nuevo secreto.
2. Nombre: OPENAI_API_KEY
3. Valor: pega tu clave → Agregar secreto

Eso es todo—nuestro código lo detectará automáticamente.

### Opción B archivo .env (si realmente necesitas uno)

```bash
cp .env.copy .env
code .env         # completa OPENAI_API_KEY=tu_clave_aquí
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->