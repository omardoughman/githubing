#!/bin/bash

           # --- 1. Create the ISO Structure ---
                                                # This is like building the "rooms" in a house
        mkdir -p build/isolinux
                               mkdir -p build/system/services
                                                             mkdir -p build/app

                                                                               # --- 2. Copy the Ingredients ---
                          # We use 'cp' so the original files stay safe in your repo
                                                                                    cp spow.py build/app/
                   cp *.service build/system/services/
                                                      cp *.codec build/system/ 2>/dev/null || echo "No codec found"

                             # --- 3. The Installation Magic ---
                                                                # This creates a script INSIDE the ISO that runs when it boots
                                        cat <<EOF > build/install.sh
                                                                    #!/bin/bash
                                                                               echo "Installing SpowOS..."
                    cp /app/spow.py /usr/local/bin/
                                                   cp /system/services/*.service /etc/systemd/system/
               systemctl enable spow-gui.service
                                                echo "Done! Restart to see the magic."
                                                                                     EOF

  chmod +x build/install.sh

                           # --- 4. Compile the ISO ---
                                                       # This command squashes everything into one .iso file
                      # (Note: On GitHub Actions, we use 'genisoimage')
                                                                       genisoimage -o spow_os.iso -R -J -V "SPOW_OS" build/

                                     echo "ISO Compiled: spow_os.iso"
                                                                     %                OmOmar@omOmOmar@oOmarOmar@OOmarOmaOmaOmOOOOOmar@omar-macbook-pro scripts % 
