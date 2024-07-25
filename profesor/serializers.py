from rest_framework import serializers
from .models import Profesor, avales_tuto, avales_biblio, Autor


class ProfesorSerializer(serializers.ModelSerializer):
    tipo_aval = serializers.SerializerMethodField()
    nombre_autor = serializers.CharField(source="autor.nombre", read_only=True)
    apellidos_autor = serializers.CharField(source="autor.apellidos", read_only=True)
    departamento_autor = serializers.CharField(
        source="autor.departamento", read_only=True
    )

    class Meta:
        model = Profesor
        fields = "__all__"

    def get_tipo_aval(self, obj):
        return "Aval de Publicación"

    def create(self, validated_data):
        print(validated_data)
        # Extraer los datos del autor del validated_data
        autor_data = {
            "nombre": validated_data["nombre"],
            "apellidos": validated_data["apellidos"],
            "departamento": validated_data["departamento"],
        }

        # Intentar crear o actualizar el autor
        autor, created = Autor.objects.update_or_create(
            nombre=autor_data.get("nombre"),
            apellidos=autor_data.get("apellidos"),
            departamento=autor_data.get("departamento"),
            defaults=autor_data,
        )

        # Crear el profesor con el autor asociado
        profesor = Profesor.objects.create(autor=autor, **validated_data)
        return profesor

    def update(self, instance, validated_data):
        # Extraer los datos del autor directamente de validated_data
        autor_data = {
            "nombre": validated_data.get("nombre"),
            "apellidos": validated_data.get("apellidos"),
            "departamento": validated_data.get("departamento"),
        }

        # Intentar crear o actualizar el autor
        autor, created = Autor.objects.update_or_create(
            nombre=autor_data.get("nombre"),
            apellidos=autor_data.get("apellidos"),
            departamento=autor_data.get("departamento"),
            defaults=autor_data,
        )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.autor = autor
        instance.save()
        return instance


class TutoSerializer(serializers.ModelSerializer):
    tipo_aval = serializers.SerializerMethodField()

    class Meta:
        model = avales_tuto
        fields = "__all__"

    def get_tipo_aval(self, obj):
        return "Aval de Tutoría"

    def create(self, validated_data):
        print(validated_data)
        # Extraer los datos del autor del validated_data
        autor_data = {
            "nombre": validated_data["nombre"],
            "apellidos": validated_data["apellidos"],
            "departamento": validated_data["departamento"],
        }

        # Intentar crear o actualizar el autor
        autor, created = Autor.objects.update_or_create(
            nombre=autor_data.get("nombre"),
            apellidos=autor_data.get("apellidos"),
            departamento=autor_data.get("departamento"),
            defaults=autor_data,
        )

        # Crear el profesor con el autor asociado
        aval_tuto = avales_tuto.objects.create(autor=autor, **validated_data)
        return aval_tuto

    def update(self, instance, validated_data):
        # Extraer los datos del autor directamente de validated_data
        autor_data = {
            "nombre": validated_data.get("nombre"),
            "apellidos": validated_data.get("apellidos"),
            "departamento": validated_data.get("departamento"),
        }

        # Intentar crear o actualizar el autor
        autor, created = Autor.objects.update_or_create(
            nombre=autor_data.get("nombre"),
            apellidos=autor_data.get("apellidos"),
            departamento=autor_data.get("departamento"),
            defaults=autor_data,
        )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.autor = autor
        instance.save()
        return instance


class BiblioSerializer(serializers.ModelSerializer):
    tipo_aval = serializers.SerializerMethodField()

    class Meta:
        model = avales_biblio
        fields = "__all__"

    def get_tipo_aval(self, obj):
        return "Aval de Bibliografía"

    def create(self, validated_data):
        print(validated_data)
        # Extraer los datos del autor del validated_data
        autor_data = {
            "nombre": validated_data["nombre"],
            "apellidos": validated_data["apellidos"],
            "departamento": validated_data["departamento"],
        }

        # Intentar crear o actualizar el autor
        autor, created = Autor.objects.update_or_create(
            nombre=autor_data.get("nombre"),
            apellidos=autor_data.get("apellidos"),
            departamento=autor_data.get("departamento"),
            defaults=autor_data,
        )

        # Crear el profesor con el autor asociado
        aval_biblio = avales_biblio.objects.create(autor=autor, **validated_data)
        return aval_biblio

    def update(self, instance, validated_data):
        # Extraer los datos del autor directamente de validated_data
        autor_data = {
            "nombre": validated_data.get("nombre"),
            "apellidos": validated_data.get("apellidos"),
            "departamento": validated_data.get("departamento"),
        }

        # Intentar crear o actualizar el autor
        autor, created = Autor.objects.update_or_create(
            nombre=autor_data.get("nombre"),
            apellidos=autor_data.get("apellidos"),
            departamento=autor_data.get("departamento"),
            defaults=autor_data,
        )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.autor = autor
        instance.save()
        return instance


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
