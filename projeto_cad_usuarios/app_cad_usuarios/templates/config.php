
<?php

$dbHost = 'Localhost';
$dbUsername = 'root';
$dbPassword ='';
$dbName = 'gs-formulario';

$conexao = new mysqli($dbHost,$dbUsername,$dbPassword,$dbName);

if($conexao->connect-erro)
{
    echo "Erro";
}
else
{
    echo "Conexão efetuada com sucesso";
}




?>
