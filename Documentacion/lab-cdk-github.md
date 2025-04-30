# 📘 Documentación del Proyecto: Laboratorio CDK + GitHub Actions

Este proyecto es un laboratorio práctico que utiliza **AWS CDK** (Cloud Development Kit) para crear y gestionar infraestructura en AWS, automatizado mediante **GitHub Actions**. A continuación, se detalla qué hace el proyecto, cómo funciona, y cómo interactúan las herramientas involucradas.

---

## 🛠️ ¿Qué es AWS CDK?

AWS CDK es un framework que permite definir infraestructura en AWS utilizando lenguajes de programación como Python, TypeScript, Java, entre otros. En lugar de escribir archivos YAML o JSON como en CloudFormation, puedes usar código para describir tus recursos.

---

## 🚀 ¿Qué crea este proyecto?

### 1. **Bucket S3**
- **Propósito**: Almacenar objetos (archivos, datos, etc.) y servir como recurso compartido para la función Lambda.
- **Configuración**:
  - Nombre: `mi-bucket-lab-cdk-github`.
  - Versionado habilitado para mantener un historial de cambios en los objetos.
  - Política de eliminación automática (`auto_delete_objects=True`) para limpiar los objetos al destruir el bucket.
  - Reglas de ciclo de vida:
    - Expiración de objetos después de 30 días.
    - Expiración de versiones no actuales después de 30 días.

### 2. **Función Lambda**
- **Propósito**: Ejecutar código en respuesta a eventos. En este caso, es una función simple que devuelve un mensaje con el nombre del bucket.
- **Configuración**:
  - Nombre: `lambda-lab-cdk-github`.
  - Memoria: 128 MB.
  - Tiempo de espera: 10 segundos.
  - Entorno: Incluye la variable `BUCKET_NAME` con el nombre del bucket S3.
  - Código: Una función en Python que devuelve un mensaje de saludo.

### 3. **Permisos**
- La función Lambda tiene permisos de lectura y escritura sobre el bucket S3.

---

## 📋 ¿Cómo funciona?

### 1. **Definición de Infraestructura**
El archivo `lab_cdk_github_stack.py` define los recursos utilizando AWS CDK. Cada recurso (S3 y Lambda) se configura con propiedades específicas.

### 2. **Automatización con GitHub Actions**
El flujo de trabajo de GitHub Actions (`cdk-deploy.yml`) permite desplegar o destruir la infraestructura desde la interfaz de GitHub. 

#### Flujo:
1. **Inputs personalizados**: Puedes elegir entre `deploy` o `destroy` al ejecutar el flujo de trabajo.
2. **Pasos principales**:
   - Configuración del entorno Python.
   - Instalación de dependencias y AWS CDK.
   - Configuración de credenciales de AWS.
   - Ejecución de `cdk deploy` o `cdk destroy` según la acción seleccionada.

### 3. **CloudFormation**
AWS CDK traduce el código en plantillas de **CloudFormation**, que luego se ejecutan para crear o actualizar los recursos en AWS. CloudFormation se encarga de:
- Gestionar el estado de los recursos.
- Manejar dependencias entre recursos.
- Proporcionar un historial de cambios.

---

## 🧪 ¿Cómo probarlo?

### Prueba manual:
1. **Despliegue**:
   - Ve a la pestaña **Actions** en GitHub.
   - Selecciona el flujo de trabajo `Deploy or Destroy AWS Infrastructure using CDK`.
   - Haz clic en **Run workflow** y selecciona `deploy`.
   - Verifica en la consola de AWS que el bucket S3 y la función Lambda se hayan creado.

2. **Prueba de la Lambda**:
   - Ve a la consola de AWS Lambda.
   - Ejecuta la función Lambda desde la consola.
   - Deberías recibir un mensaje como:
     ```json
     {
       "statusCode": 200,
       "body": "Hello from Lambda! Using bucket mi-bucket-lab-cdk-github"
     }
     ```

3. **Destrucción**:
   - Ejecuta el flujo de trabajo nuevamente, seleccionando `destroy`.
   - Verifica que los recursos se hayan eliminado.

---

## 🔄 Interacción entre GitHub Actions y AWS

1. **GitHub Actions**:
   - Automatiza el despliegue y destrucción de la infraestructura.
   - Usa las credenciales de AWS configuradas como secretos (`AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY`).
   - Ejecuta comandos de CDK (`cdk deploy` o `cdk destroy`).

2. **AWS CDK**:
   - Traduce el código Python en plantillas de CloudFormation.
   - Envía las plantillas a AWS para que CloudFormation gestione los recursos.

3. **CloudFormation**:
   - Crea, actualiza o elimina los recursos según las plantillas generadas por CDK.
   - Proporciona un historial de cambios y estado de los recursos.

---

## ⚖️ Diferencias entre CDK y Terraform

| **Aspecto**            | **AWS CDK**                                     | **Terraform**                                  |
|-------------------------|------------------------------------------------|-----------------------------------------------|
| **Lenguaje**            | Usa lenguajes de programación (Python, TS, etc.)| Usa HCL (HashiCorp Configuration Language).   |
| **Estado**              | Gestionado por CloudFormation.                 | Gestionado localmente o en un backend remoto. |
| **Ecosistema**          | Integrado con AWS.                             | Multicloud (AWS, Azure, GCP, etc.).           |
| **Curva de aprendizaje**| Más fácil para desarrolladores.                | Más fácil para administradores de sistemas.   |
| **Automatización**      | Usa CloudFormation para despliegues.           | Usa su propio motor de despliegue.            |

---

## 📊 Diagrama de Arquitectura

```plaintext
+-------------------+        +-------------------+
| GitHub Actions    |        | AWS CDK           |
| - cdk deploy      | -----> | - Genera plantillas|
| - cdk destroy     |        | - Traduce a CFN    |
+-------------------+        +-------------------+
                                    |
                                    v
                          +-------------------+
                          | AWS CloudFormation|
                          | - Gestiona recursos|
                          +-------------------+
                                    |
                                    v
                          +-------------------+
                          | AWS Resources     |
                          | - S3 Bucket       |
                          | - Lambda Function |
                          +-------------------+