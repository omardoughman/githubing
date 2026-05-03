/* ================================
   FM STEREO TRANSMITTER CONFIG
   File: fm_config.h
   ================================ */

/* Audio files */
#define AUDIO_LEFT_FILE   "left.wav"
#define AUDIO_RIGHT_FILE  "right.wav"

/* FM parameters */
#define CARRIER_FREQUENCY 100000000   // 100 MHz
#define SAMPLE_RATE       240000
#define FREQ_DEVIATION    75000        // 75 kHz

/* Stereo settings */
#define PILOT_FREQ        19000
#define SUBCARRIER_FREQ   38000
#define PILOT_GAIN        0.10

/* Output */
#define IQ_OUTPUT_FILE    "fm_stereo_iq.raw"

/* UI defaults */
#define MASTER_VOLUME     1.0
/* FM CONFIG */

#define AUDIO_LEFT_FILE   "left.wav"
#define AUDIO_RIGHT_FILE  "right.wav"

#define SAMPLE_RATE       240000
#define FREQ_DEVIATION    75000
#define CARRIER_FREQ      100000000

#define IQ_OUTPUT_FILE    "fm_iq.raw"
