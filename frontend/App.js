import React, { useState } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Image, Alert } from 'react-native';

export default function App() {
  const [photo, setPhoto] = useState(null);
  const [aiResult, setAiResult] = useState("Waiting for harvest scan...");
  const [mandiSlot, setMandiSlot] = useState("No slot booked yet");

  // Mock function simulating an offline AI scan of crop quality
  const scanCropQuality = () => {
    setAiResult("🔄 Processing Image Offline...");
    
    setTimeout(() => {
      setAiResult("✅ AI Grading Result: GRADE-A (Excellent Quality Fresh Crop)");
      setMandiSlot("🎫 Assigned Mandi Slot Token: #M3-2309 (Reporting Time: 10:00 AM)");
      Alert.alert("Scan Successful!", "Your harvest is graded. Mandi entry token generated safely.");
    }, 1500);
  };

  return (
    <View style={styles.container}>
      {/* App Header Area */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>KrishiSetu AI 🌾</Text>
        <Text style={styles.headerSubtitle}>Smart Farm-to-Market Connect</Text>
      </View>

      {/* Camera Viewfinder Mock Area */}
      <View style={styles.card}>
        <Text style={styles.cardHeader}>📸 CROP SCANNER ENGINE</Text>
        <View style={styles.cameraPlaceholder}>
          <Text style={styles.placeholderText}>[ Camera Viewfinder Active ]</Text>
        </View>
        
        <TouchableOpacity style={styles.primaryButton} onPress={scanCropQuality}>
          <Text style={styles.buttonText}>CAPTURE & ANALYZE CROP</Text>
        </TouchableOpacity>
      </View>

      {/* AI Inference Data & Token Response Output Display */}
      <View style={styles.resultCard}>
        <Text style={styles.resultTitle}>📊 LIVE LOGISTICS STATUS</Text>
        <Text style={styles.dataLabel}>Quality Rating:</Text>
        <Text style={styles.dataValue}>{aiResult}</Text>
        
        <Text style={styles.dataLabel}>Market Token status:</Text>
        <Text style={styles.tokenValue}>{mandiSlot}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#F4F6F4', padding: 20, justifyContent: 'center' },
  header: { alignItems: 'center', marginBottom: 25 },
  headerTitle: { fontSize: 32, fontWeight: 'bold', color: '#1B5E20' },
  headerSubtitle: { fontSize: 14, color: '#4E342E', marginTop: 4, fontWeight: '500' },
  card: { backgroundColor: '#FFF', borderRadius: 16, padding: 20, elevation: 4, shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.1, shadowRadius: 4, marginBottom: 20 },
  cardHeader: { fontSize: 16, fontWeight: '700', color: '#37474F', marginBottom: 12, textAlign: 'center' },
  cameraPlaceholder: { width: '100%', height: 180, backgroundColor: '#ECEFF1', borderRadius: 12, justifyContent: 'center', alignItems: 'center', borderStyle: 'dashed', borderWidth: 2, borderColor: '#B0BEC5', marginBottom: 16 },
  placeholderText: { color: '#78909C', fontWeight: '600' },
  primaryButton: { backgroundColor: '#2E7D32', paddingVertical: 14, borderRadius: 10, alignItems: 'center' },
  buttonText: { color: '#FFF', fontSize: 15, fontWeight: 'bold', letterSpacing: 0.5 },
  resultCard: { backgroundColor: '#E8F5E9', borderRadius: 16, padding: 20, borderWidth: 1, borderColor: '#C8E6C9' },
  resultTitle: { fontSize: 15, fontWeight: '700', color: '#2E7D32', marginBottom: 10 },
  dataLabel: { fontSize: 12, color: '#558B2F', marginTop: 8, fontWeight: '600', textTransform: 'uppercase' },
  dataValue: { fontSize: 15, color: '#263238', fontWeight: '700', marginTop: 2 },
  tokenValue: { fontSize: 15, color: '#E65100', fontWeight: '700', marginTop: 2 }
});
        
