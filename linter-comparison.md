# Comparación entre distintos linters de Python

## Ruff
**Ruff** es un linter open-source para Python desarrollado por Astral. Este contiene corrección automática de errores, 
cientas de reglas built-in y varias integraciones de edición.
Ruff es reconocido principalmente por su velocidad.

### Features de Ruff
Las features principales de Ruff incluyen herramientas tales como:
* Ser entre diez y cien veces más veloz que otros linters.
* Tiene un auto-fix disponible.
* Integraciones de edición.
* Cacheo integrado.
* Instalable vía pip.

El highlight principal de Ruff, como fue mencionado previamente, es su velocidad. La homepage de Python lo describe como
hasta cien veces más veloz que el resto de los linters de Python existentes. Esta cualidad hace que sea el linter ideal 
para los desarrolladores que buscan elevar su productividad y ahorrar tiempo. 

Ruff soporta hasta 700 reglas de linteo inspiradas por herramientas populares tales como **pyupgrade, Flake8 y pysort**.

Otra herramienta importante de Ruff es el cacheo integrado. Este feature elimina la necesidad de reanalizar archivos que
no fuerom modificados. Mientras que su feature de auto-fix permite ahorrar tiempo con su corrección automática de errores.

### Ventajas de Ruff
Las principales ventajas de Ruff son:
- Su velocidad
- Su auto-fix
- Resultados casi instantáneos
- Altamente configurable
- Es gratis

La ventaja principal de Ruff es su velocidad. Los usuarios se han pronunciado sobre lo rápido que es. Mientras que la 
performance rápida de Ruff le ahorra tiempo a los desarrolladores, también lo hace el auto-fix que corrige automáticamente
los errores, haciendo que no tenga que corregirlos manualmente el usuario. 
Los algoritmos optimizados de Ruff, que están escritos en Rust, ofrecen una ejecución rápida. La herramienta de linteo 
analiza el código y ofrece resultados casi instantáneos.

### Contras de Ruff

Las contras de Ruff incluyen:
- Es relativamente nuevo
- Soporte de plugins
- Problemas al agregar reglas customizadas

Ya que Ruff es un linter nuevo, su comunidad y seguidores no es tan grande como la de otros linters. De este modo, hay 
menos soporte o recursos disponibles hasta que crezca su popularidad. Esto puede hacer que los errores o bugs sean más 
difíciles de solucionar.

Las últimas dos contras de Ruff, según sus usuarios es el hecho de que esperan que soporte más plugins, y la segunda es 
que, debido a que es una herramienta compilada, usuarios han notado problemas al querer agregar reglas propias.

### Usuarios de Ruff reconocidos
- **Amazon (AWS SAM)**
- **FastAPI**
- **Jupyter**
- **Mozilla Firefox**
- **Neon**
- **Pandas**
- **Pytorch**
- **meson-python**
- **nox**
- **pip**



## Flake8

Flake8 es un linter de Python de código abierto altamente customizable. Es conocido por su exactitud y su baja cantidad 
de falsos positivos. Este provee consistencia de código y ayuda a los desarrolladores a asegurarse de que su código es 
mantenible y legible

### Features de Flake8
Las herramientas principales de linteo incluyen:

- Adhesión a la guía **PEP 8.**
- Una gran cantidad de optimizaciones
- Extensibilidad
- Integraciones
- Violaciones de estilos
- Errores de sintáxis
- Análisis de complejidad de código
- Imports y variables sin uso

Flake8 refuerza el cumplimiento de la guia de estiloPEP8 (Python Enhancement Proposal). Se adhiere a estándares para
convenciones de nombres, identaciones, layout, etc. La herramientas de linteo promueve legibilidad de código y consistencia

Flake8 puede customizarse para que se adecúe a las preferencias estilísticas del código que el desarrollador desee. 

Los desarrolladores pueden usar Flake8 para encontrar inconsistencias en el código. Esto logra 
una mejora en la legibilidad y mantenibilidad, además de detectar errores de sintáxis como identaciones incorrectas o dos
puntos faltantes. 
Este linter detecta bloques de código complejo que puedan necesitar una simplificación/refactoring. 

### Pros of Flake8
Ventajas de usar Flake8 como linter:
- Es código abierto
- Es muy exacto.
- Ampliamente usado
- Muchas customizaciones

El hecho de que Flake8 sea open-source es un plus para los que buscan un linteo libre. Su seguridad, que produce muy pocos
falsos positivos, facilita la vida de los desarrolladores. 

Debido al hecho de que muchos usuarios lo consideran como el estándar para el linteo de código de Python, los nuevos 
usuarios encuentran recursos y soporte de forma fácil. 

Además, si un equipo de desarrollo tiene guías de codificación únicas, Flake8 puede acomodarse a ellas con reglas custom
de linteo que coincida con las preferencias y estándares de cada proyecto.

### Contras de Flake8
Las desventajas de usar Flake8 incluyen:

- Difícil de entender en un principio
- Muy rígido

Los principiantes pueden necesitar tiempo para adaptarse a Flake8 en un principio. Y algunos usuarios pueden notar
que la rígida adhesión a PEP8 muy estricta para sus preferencias de codeo. 


## Codacy
Codacy (también conocido como Codacy Quality) es una herramienta de linting flexible que soporta más de cuarenta lenguajes
y multiples integraciones con herramientas externaes tales como Hira, Slack, Github y Gitlab. Puede ayudar a los desarrolladores
a encontrar problemas en el código tales como errores y vulnerabilidades de seguridad.
Este tiene un plan gratis y uno pago. 

### Features de Codacy

Algunas features de Codacy pueden ser:
* Checks automáticos
* Sugerencias de un clic
* Integraciones
* Soportan múltiples lenguajes de programación
* Configuraciones personalizadas
* Estándares de codificación
* Interfaz de usuario

Las features de Codacy comienzan con una interfaz intuitiva que es fácil de usar. 
La herramienta de linteo checkean automáticamente commits/PRs cuando ocurren y provee un feedback instantáneo dentro del
sistema de control de versiones utilizado (GitHub, GitLab o Bitbucket). Codacy también ofrece sugerencias de commit one-click, y
bloquea merges incorrectos para ayudar a los desarrolladores a optimizar su calidad de código con un esfuerzo manual mínimo.

Codacy se integra con Slack para brindar notificaciones instantáneas cuando se detectan issues.

Otras herramientas intereasntes son, su versatilidad para soportar más de cuarenta lenguajes de programación/ecosistemas,
y sus dashboards que ofrecen configuraciones personalizadas.

### Pros de Codacy
Los fuertes de Codacy incluyen:
* Interfaz intuitiva
* Reportes detallados
* Integraciones sólidas
* Soporte multilenguaje

### Contras de Codacy 
Las debilidades de Codacy incluyen:
* La necesidad de pago para prestaciones avanzadas
* Performance lenta
* Configuración compleja

Aunque que Codacy Quality tiene un plan open-source que es libre para desarrolladores, desbloquear prestaciones avanzadas
como integraciones con VCSs, one click autofixes, etc, requiere del pago de un plan premium, que ronda los quince dolares.


## Conclusiones

### ¿Qué se busca en un Linter de Python?

Para elegir el mejor linter de Python, los programadores considerarán varios factores al elegir su linter de preferencia.
Empezando con:
* Que sea de uso fácil
* Curva de aprendizaje pequeña
* Que tenga buena y variada documentación y soporte de la comunidad
* Compatibilidad con versiones, librerías y frameworks de Python
* Que sea configurable y personalizable
* Que tenga integraciones con herramientas de desarrollo popoulares e IDEs.

Los usuarios tienden a buscar una herramienta de linteo de Python cuya curva de aprendizaje sea minima, tanto para los
desarrolladores novatos como para los experimentados. Además, también se busca un linter actualizado y mantenido periódicamente.

Finalmente, resulta importante notar que, el linter elegido a la hora de desarrollar un proyecto debe ser compatible con
la versión, librería y frameworks que se esté usando para el proyecto en cuestión, y debe integrarse bien con el entorno
de desarrollo o editor de texto que se use. Este también debe ser altamente configurable para que encaje con las preferencias
del equipo de desarrollo. Y, siendo exigentes, sería bueno que el lintger incluya chequeo de tipos, reportaje de errores
formateo de código automático y detección de errores de sintáxis en tiempo real. 














