# FaceLock Architecture

## Workflow

1. User launches the FaceLock application.
2. The webcam captures the user's face.
3. The system compares the captured face with the registered face.
4. If the face matches:
   - Access is granted.
   - User can encrypt or decrypt files.
5. If the face does not match:
   - Access is denied.

## Modules

- face_auth
  - Face detection
  - Face encoding
  - Face authentication

- encryption
  - File encryption
  - File decryption

- data
  - Stored face data
  - Encrypted files