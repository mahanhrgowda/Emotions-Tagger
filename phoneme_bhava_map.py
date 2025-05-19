# Phoneme-to-Bhāva–Chakra–Rasa–Color map
# Based on Maheshwara Sūtras and classical Sanskrit dramaturgy

PHONEME_BHAVA_MAP = {
    # Gutturals
    'ka': ('Jñāna (Wisdom)', 'Ājñā', 'Adbhuta (Wonder)', '#2980b9'),
    'kha': ('Utsāha (Energy)', 'Maṇipūra', 'Vīra (Heroism)', '#f39c12'),
    'ga': ('Āśraya (Support)', 'Anāhata', 'Karuṇā (Compassion)', '#2ecc71'),
    'gha': ('Tapas (Austerity)', 'Mūlādhāra', 'Raudra (Anger)', '#c0392b'),
    'ṅa': ('Nididhyāsana (Contemplation)', 'Sahasrāra', 'Śānta (Peace)', '#9b59b6'),

    # Palatals
    'ca': ('Viveka (Discernment)', 'Ājñā', 'Adbhuta (Wonder)', '#16a085'),
    'cha': ('Pravṛtti (Action)', 'Maṇipūra', 'Vīra (Heroism)', '#d35400'),
    'ja': ('Bodha (Realization)', 'Viśuddha', 'Śṛṅgāra (Love)', '#fd79a8'),
    'jha': ('Śuddhi (Purification)', 'Viśuddha', 'Bībhatsa (Disgust)', '#8e44ad'),
    'ña': ('Sneha (Affection)', 'Anāhata', 'Karuṇā (Compassion)', '#27ae60'),

    # Retroflex
    'ṭa': ('Dhṛti (Steadfastness)', 'Mūlādhāra', 'Vīra (Heroism)', '#e74c3c'),
    'ṭha': ('Śaurya (Bravery)', 'Svādhiṣṭhāna', 'Raudra (Anger)', '#d63031'),
    'ḍa': ('Dāna (Charity)', 'Anāhata', 'Vīra (Heroism)', '#f1c40f'),
    'ḍha': ('Samarpana (Surrender)', 'Anāhata', 'Śānta (Peace)', '#a29bfe'),
    'ṇa': ('Śraddhā (Faith)', 'Sahasrāra', 'Śānta (Peace)', '#6c5ce7'),

    # Dentals
    'ta': ('Dhairya (Courage)', 'Maṇipūra', 'Vīra (Heroism)', '#f39c12'),
    'tha': ('Ārjava (Integrity)', 'Svādhiṣṭhāna', 'Śānta (Peace)', '#f7dc6f'),
    'da': ('Dāna (Giving)', 'Anāhata', 'Karuṇā (Compassion)', '#f9ca24'),
    'dha': ('Śakti (Power)', 'Maṇipūra', 'Raudra (Anger)', '#e67e22'),
    'na': ('Karunā (Compassion)', 'Anāhata', 'Karuṇā (Compassion)', '#2ecc71'),

    # Labials
    'pa': ('Tapasya (Austerity)', 'Mūlādhāra', 'Raudra (Fierce)', '#c0392b'),
    'pha': ('Utsāha (Effort)', 'Svādhiṣṭhāna', 'Vīra (Heroism)', '#e67e22'),
    'ba': ('Prem (Love)', 'Anāhata', 'Śṛṅgāra (Romance)', '#e84393'),
    'bha': ('Vikāsa (Expansion)', 'Sahasrāra', 'Adbhuta (Amazement)', '#9b59b6'),
    'ma': ('Śāntiḥ (Peace)', 'Sahasrāra', 'Śānta (Tranquility)', '#95a5a6'),

    # Semivowels
    'ya': ('Ānanda (Bliss)', 'Sahasrāra', 'Hāsya (Joy)', '#f39c12'),
    'ra': ('Vīraḥ (Heroism)', 'Mūlādhāra', 'Vīra (Courage)', '#e74c3c'),
    'la': ('Prema (Love)', 'Anāhata', 'Śṛṅgāra (Beauty)', '#ff7675'),
    'va': ('Sphūrti (Inspiration)', 'Viśuddha', 'Adbhuta (Surprise)', '#74b9ff'),

    # Sibilants + Aspirate
    'śa': ('Bhaktiḥ (Devotion)', 'Sahasrāra', 'Śānta (Serenity)', '#8e44ad'),
    'ṣa': ('Āstikya (Faith)', 'Ājñā', 'Śānta (Reverence)', '#6c5ce7'),
    'sa': ('Dharma (Righteousness)', 'Viśuddha', 'Vīra (Justice)', '#3498db'),
    'ha': ('Mokṣa (Liberation)', 'Sahasrāra', 'Śānta (Transcendence)', '#9b59b6'),

    # Vowels (generic)
    'a': ('Satya (Truth)', 'All', 'Śānta (Calm)', '#ecf0f1'),
    'ā': ('Ānanda (Joy)', 'Anāhata', 'Hāsya (Joy)', '#f39c12'),
    'i': ('Medhā (Intellect)', 'Ājñā', 'Adbhuta (Wisdom)', '#3498db'),
    'ī': ('Prīti (Delight)', 'Sahasrāra', 'Śṛṅgāra (Tenderness)', '#fd79a8'),
    'u': ('Ojas (Vitality)', 'Maṇipūra', 'Vīra (Power)', '#f1c40f'),
    'ū': ('Śakti (Force)', 'Svādhiṣṭhāna', 'Raudra (Energy)', '#e67e22'),
    'e': ('Sattva (Clarity)', 'Viśuddha', 'Śānta (Balance)', '#a3cb38'),
    'ai': ('Cetanā (Consciousness)', 'Sahasrāra', 'Adbhuta (Awakening)', '#81ecec'),
    'o': ('Sampatti (Wealth)', 'Anāhata', 'Śṛṅgāra (Elegance)', '#fab1a0'),
    'au': ('Vistāra (Expansion)', 'Sahasrāra', 'Adbhuta (Grandeur)', '#ffeaa7'),
    'ṁ': ('Bindu (Point)', 'Sahasrāra', 'Śānta (Silence)', '#bdc3c7'),
    'ḥ': ('Praśānti (Stillness)', 'Sahasrāra', 'Śānta (Stillness)', '#dcdde1'),
}
