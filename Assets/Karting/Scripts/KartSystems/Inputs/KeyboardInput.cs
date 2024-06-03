using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

namespace KartGame.KartSystems {
    public class KeyboardInput : BaseInput {
        private string apiURL = "http://127.0.0.1:5000/treadmill"; // Set your API endpoint URL here

        private void Start() {
            StartCoroutine(GetControlInputs());
        }

        private IEnumerator GetControlInputs() {
            while (true) { // Continuous loop to keep fetching data
                using (UnityWebRequest webRequest = UnityWebRequest.Get(apiURL)) {
                    yield return webRequest.SendWebRequest();
                    
                    if (webRequest.isNetworkError || webRequest.isHttpError) {
                        Debug.LogError("Network Error: " + webRequest.error);
                    } else {
                        ProcessApiResponse(webRequest.downloadHandler.text);
                    }
                }
                yield return new WaitForSeconds(0.1f); // Delay before the next API request
            }
        }

        private void ProcessApiResponse(string jsonResponse) {
            ControlData data = JsonUtility.FromJson<ControlData>(jsonResponse);
            inputData.Accelerate = data.Accelerate;
            inputData.Brake = data.Brake;
            inputData.TurnInput = data.Horizontal;
        }

        private InputData inputData = new InputData();

        public override InputData GenerateInput() {
            return inputData;
        }

        [System.Serializable]
        private class ControlData {
            public float Horizontal;
            public bool Brake;
            public bool Accelerate;
        }
    }
}
