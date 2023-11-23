
pushd "%~dp0\..\"
set PROG_HOME=%cd%
popd
set SPARK_HOME="%PROJECT_HOME%\venv\Lib\site-packages\pyspark"
if not defined SPARK_HOME ( 
    echo "SPARK_HOME must be set to the location of a Spark distribution!"
    Exit /b
)
echo "Starting Spark Kernel with SPARK_HOME=%SPARK_HOME%"
rem for /f %%i in ('dir /B toree-assembly-*.jar') do set KERNEL_ASSEMBLY=%%i popd
rem disable randomized hash for string in Python 3.3+
set PYTHONHASHSEED=0
rem set TOREE_ASSEMBLY=%PROG_HOME%/lib/%KERNEL_ASSEMBLY%
rem The SPARK_OPTS values during installation are stored in __TOREE_SPARK_OPTS__. This allows values to be specified during
rem install, but also during runtime. The runtime options take precedence over the install options.
if not defined SPARK_OPTS (
    if defined __TOREE_SPARK_OPTS__ (
        set SPARK_OPTS=%__TOREE_SPARK_OPTS__%
    )
)
if not defined TOREE_OPTS (
    if defined __TOREE_SPARK_OPTS__ (
        set TOREE_OPTS=%__TOREE_OPTS__%
    )
)
"%JAVA_HOME%\bin\java" -cp "%SPARK_HOME%\jars\*;%PROG_HOME%\lib\toree-assembly-0.5.0-incubating.jar;." -Dscala.usejavacp=true org.apache.spark.deploy.SparkSubmit %SPARK_OPTS% --class org.apache.toree.Main %PROG_HOME%\lib\toree-assembly-0.5.0-incubating.jar %TOREE_OPTS% %*
