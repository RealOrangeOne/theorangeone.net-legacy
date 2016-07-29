title: Astrill Extractor
template: projects
slug: astrill-extractor
repo: https://gist.github.com/RealOrangeOne/050da86871fb952ba7bfe97eece8555c

Astrill, my VPN of choice, allows you to export OpenVPN config files for all it's VPNs, allowing you to connect on platforms it doesn't provide clients for. The AUR package `astrill` has started becoming really unstable on my machine, so I decided to switch it out for these VPN files, as gnome has excellent support for OpenVPN.

The export step is really simple, you just login to the web portal, create an entry for your machine, and export the config files. Their tutorial for this can be found [here](http://wiki.astrill.com/index.php/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_Network_Manager_on_Linux). The problem with this is that some applications wont accept the certificates embedded into the file like this. (Gnome does, but I only realised that whilst writing this). So I started writing a simple parser to extract the certificates from the config files, and saving them as separate files.


<script src="https://gist.github.com/RealOrangeOne/050da86871fb952ba7bfe97eece8555c.js"></script>

The above script will split out the files and save them into separate directories for each config file. These files can then be imported and used in an openvpn-compatable application.

### Is it even needed?
Certain network-manager packages actually supports importing `.ovpn` files directly, and sets everything up for you, including the files for the keys etc, without needing to extract them before. This does make my script useless to me, but hopefully someone will find it useful!
