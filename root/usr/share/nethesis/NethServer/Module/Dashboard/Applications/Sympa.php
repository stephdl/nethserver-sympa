<?php
namespace NethServer\Module\Dashboard\Applications;

/**
 * sympa web interface
 *
 * @author stephane de labrusse
 */
class Sympa extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "Sympa";
    }

    public function getInfo()
    {
         $host = explode(':',$_SERVER['HTTP_HOST']);
         return array(
            'url' => "https://".$host[0]."/sympa",
         );
    }
}
