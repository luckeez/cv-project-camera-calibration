import cv2

# Funzione di callback per ottenere le coordinate del punto cliccato
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Stampa le coordinate su console
        print(f"[{x}, {y}],")
        
        # Scrivi le coordinate nel file di log
        with open('coordinates_log.txt', 'a') as f:
            f.write(f"[{x}, {y}],\n")
        
        # Mostra il punto selezionato sull'immagine
        cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
        cv2.imshow('image', img)

# Carica l'immagine
image_path = 'view3.png'  # Sostituisci con il percorso della tua immagine
img = cv2.imread(image_path)

# Mostra l'immagine in una finestra
cv2.imshow('image', img)

# Imposta la funzione di callback per il clic del mouse
cv2.setMouseCallback('image', click_event)

# Aspetta la chiusura della finestra
cv2.waitKey(0)

# Distruggi tutte le finestre aperte
cv2.destroyAllWindows()

