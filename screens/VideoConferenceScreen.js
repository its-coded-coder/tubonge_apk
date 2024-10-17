import React, { useState, useEffect } from 'react';
import { View, Text, Button } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { auth } from '../firebaseConfig';
import { getFirestore, collection, addDoc, onSnapshot } from 'firebase/firestore';

const VideoConferenceScreen = () => {
  const [rooms, setRooms] = useState([]);
  const navigation = useNavigation();
  const db = getFirestore();

  useEffect(() => {
    const unsubscribe = onSnapshot(collection(db, 'rooms'), (snapshot) => {
      const roomsData = snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }));
      setRooms(roomsData);
    });

    return () => unsubscribe();
  }, []);

  const createRoom = async () => {
    const room = await addDoc(collection(db, 'rooms'), { name: 'New Room' });
    navigation.navigate('Room', { roomId: room.id });
  };

  return (
    <View>
      <Text>Video Conference Rooms</Text>
      {rooms.map((room) => (
        <Button key={room.id} title={room.name} onPress={() => navigation.navigate('Room', { roomId: room.id })} />
      ))}
      <Button title="Create Room" onPress={createRoom} />
    </View>
  );
};

export default VideoConferenceScreen;
